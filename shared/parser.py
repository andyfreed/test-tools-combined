import re
import pandas as pd
from typing import Dict, List, Tuple

class ExamParser:
    def __init__(self):
        # Updated pattern to fix invalid escape sequence and handle company names with Inc., Ltd., etc.
        self.question_pattern = r'(\d+)\.\s*(.*?)(?=\s*(?:\n[A-Da-d]\.|\Z))'
        # Modified answer pattern to be more strict about answer format and fix escape sequence
        self.answer_pattern = r'(?:^|\n)\s*([A-Da-d])\.\s*(.*?)(?=\s*(?:\n[A-Da-d]\.|\Z|\n\d+\.|\Z))'

    def parse_answer_key(self, answer_key_content: str) -> Dict[str, str]:
        """Parse answer key content into a dictionary."""
        if not answer_key_content:
            return {}

        answers = {}

        # Simple pattern to match question number and answer letter
        # This pattern looks for "number: letter" format
        pattern = r'(\d+)\s*:\s*([A-Da-d])'

        matches = re.finditer(pattern, answer_key_content, re.MULTILINE | re.IGNORECASE)
        for match in matches:
            question_num, answer_letter = match.groups()
            # Clean up and store the answer
            answers[question_num.strip()] = answer_letter.strip().upper()

        # Debug print
        print("Found answers:", answers)

        return answers

    def parse_content(self, content: str, answer_key_content: str = None) -> List[Dict]:
        """Parse exam content into structured format."""
        content = content.replace('\r\n', '\n').replace('\r', '\n')
        parsed_questions = []

        # Parse answer key if provided
        answer_key = self.parse_answer_key(answer_key_content) if answer_key_content else {}

        # Split content into question blocks
        questions_raw = re.split(r'\n(?=\d+\.)', content)

        for question_block in questions_raw:
            try:
                # Skip empty blocks
                if not question_block.strip():
                    continue

                # Match question
                question_match = re.match(self.question_pattern, question_block, re.DOTALL | re.MULTILINE)
                if not question_match:
                    continue

                question_num = question_match.group(1)
                question_text = question_match.group(2).strip().strip('"')

                # Skip if it's just a year
                if question_text.isdigit():
                    continue

                # Initialize answers with empty strings
                answers = {'A': '', 'B': '', 'C': '', 'D': ''}
                correct_answer_text = ''

                # Get the answer section after the question
                answer_section = question_block[len(question_match.group(0)):].strip()

                # Find all answer choices
                answer_matches = list(re.finditer(self.answer_pattern, '\n' + answer_section, re.DOTALL | re.MULTILINE))

                # Process each answer choice
                for match in answer_matches:
                    letter, text = match.groups()
                    letter = letter.upper()
                    text = text.strip().strip('"').strip()

                    if text:  # Only store non-empty answers
                        answers[letter] = text

                        # Check for asterisk marking correct answer
                        if '*' in text:
                            correct_answer_text = text.replace('*', '').strip()
                            answers[letter] = correct_answer_text

                # Check answer key
                if not correct_answer_text and question_num in answer_key:
                    correct_letter = answer_key[question_num]
                    if correct_letter in answers:
                        correct_answer_text = answers[correct_letter]

                # Only add if we have a question
                if question_text:
                    question_dict = {
                        'Question': question_text,
                        'answer choice A': answers['A'],
                        'answer choice B': answers['B'],
                        'answer choice C': answers['C'],
                        'answer choice D': answers['D'],
                        'Correct Answer': correct_answer_text
                    }
                    parsed_questions.append(question_dict)

            except Exception as e:
                print(f"Error parsing question: {str(e)}")
                continue

        return parsed_questions

    def create_dataframe(self, parsed_questions: List[Dict]) -> pd.DataFrame:
        """Convert parsed questions to pandas DataFrame."""
        if not parsed_questions:
            return pd.DataFrame(columns=['Question', 'answer choice A', 'answer choice B', 
                                      'answer choice C', 'answer choice D', 'Correct Answer'])
        return pd.DataFrame(parsed_questions)

    def process_file(self, content: str, answer_key_content: str = None) -> pd.DataFrame:
        """Process file content and return DataFrame."""
        parsed_questions = self.parse_content(content, answer_key_content)
        return self.create_dataframe(parsed_questions) 