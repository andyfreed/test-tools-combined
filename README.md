# CSV to XLSX Converter

A Streamlit web application that converts CSV files to XLSX format with specific column mapping requirements for CFP Board course data.

## Features

- Upload CSV files
- Preview input data
- Automatic column mapping:
  - CFP Board Course ID → CFP Program ID (General format, no commas)
  - Completed → Date Individual Completed (Short date format)
  - License number → Attendee CFP Board ID (General format, no commas)
  - Last name → attendee last name
  - First name → attendee first name
- Download converted XLSX files with proper formatting

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
python -m streamlit run main.py
```

2. Open your web browser and navigate to `http://localhost:8501`
3. Upload your CSV file
4. Preview the conversion
5. Download the converted XLSX file

## Requirements

- Python 3.6+
- streamlit
- pandas
- openpyxl 