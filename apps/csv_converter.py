import streamlit as st
import pandas as pd
import io
from utils import process_file
from openpyxl.styles import numbers, Border, Side
from shared.common import app_header, app_footer, display_success

def main():
    app_header(
        "CSV to XLSX Converter",
        """This application converts CSV files to XLSX format with specific column mapping:
        - CFP Board Course ID → CFP Program ID (General format, no commas)
        - Completed → Date Individual Completed (Short date format)
        - License number → Attendee CFP Board ID (General format, no commas) 
        - Last name → attendee last name
        - First name → attendee first name"""
    )

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        try:
            # Read CSV file
            df = pd.read_csv(uploaded_file)

            # Show input data preview
            st.markdown('<div class="sub-header">Input Data Preview</div>', unsafe_allow_html=True)
            st.dataframe(df.head())

            try:
                # Process the file
                df_processed = process_file(df)

                # Show processed data preview
                st.markdown('<div class="sub-header">Processed Data Preview</div>', unsafe_allow_html=True)
                st.dataframe(df_processed.head())

                # Create download button
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl', datetime_format='mm/dd/yyyy') as writer:
                    df_processed.to_excel(writer, index=False, sheet_name='Sheet1')

                    # Get the workbook and worksheet
                    workbook = writer.book
                    worksheet = writer.sheets['Sheet1']

                    # Get column indices
                    cfp_program_id_col = df_processed.columns.get_loc('CFP Program ID') + 1
                    attendee_id_col = df_processed.columns.get_loc('Attendee CFP Board ID') + 1

                    # Apply formatting to numeric columns
                    # CFP Program ID: General format, no commas
                    for row in range(2, len(df_processed) + 2):  # Skip header row
                        cell = worksheet.cell(row=row, column=cfp_program_id_col)
                        cell.number_format = numbers.FORMAT_GENERAL

                    # Attendee CFP Board ID: Number format without decimals
                    for row in range(2, len(df_processed) + 2):  # Skip header row
                        cell = worksheet.cell(row=row, column=attendee_id_col)
                        cell.number_format = numbers.FORMAT_NUMBER

                    # Remove cell borders for all cells
                    no_border = Border(left=Side(style=None), 
                                       right=Side(style=None),
                                       top=Side(style=None),
                                       bottom=Side(style=None))

                    for row in worksheet.rows:
                        for cell in row:
                            cell.border = no_border

                output.seek(0)

                # Add file name input field
                output_filename = st.text_input(
                    "Enter the output file name",
                    value="converted_file.xlsx",
                    help="Enter the name for your output Excel file (must end with .xlsx)"
                )

                # Ensure filename ends with .xlsx
                if not output_filename.endswith('.xlsx'):
                    output_filename += '.xlsx'

                st.download_button(
                    label="Download XLSX file",
                    data=output,
                    file_name=output_filename,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

                # Show success message with statistics
                success_msg = f"""
                Conversion completed successfully!
                - Total records processed: {len(df_processed)}
                - Columns mapped: {len(df_processed.columns)}
                """
                display_success(success_msg)

            except ValueError as e:
                st.error(f"Error processing file: {str(e)}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

        except Exception as e:
            st.error(f"Error reading CSV file: {str(e)}")
    
    app_footer()

if __name__ == "__main__":
    main()