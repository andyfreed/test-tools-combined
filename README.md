# File Converter Tools

A collection of file conversion tools, starting with a CSV to XLSX converter that handles specific formatting requirements for CFP Board course data.

## Features

- CSV to XLSX Converter:
  - Upload CSV files
  - Preview input data
  - Automatic column mapping:
    - CFP Board Course ID → CFP Program ID (General format, no commas)
    - Completed → Date Individual Completed (Short date format)
    - License number → Attendee CFP Board ID (General format, no commas)
    - Last name → attendee last name
    - First name → attendee first name
  - Download converted XLSX files with proper formatting
- Multi-app support in single Azure instance
- User-friendly Streamlit interface

## Project Structure

```
FileConverterTools/
├── apps/                    # Directory for all applications
│   └── csv_converter.py     # CSV to XLSX converter application
├── main.py                  # Main router for multiple apps
├── requirements.txt         # Project dependencies
└── utils.py                 # Shared utilities
```

## Adding New Apps

1. Create a new Python file in the `apps` directory
2. Add a `main()` function to your app
3. Import and add it to the `APPS` dictionary in `main.py`:
```python
from apps.new_app import main as new_app_main

APPS = {
    "CSV to XLSX Converter": csv_converter_app,
    "New App": new_app_main,
}
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/andyfreed/CsvXlsxTransformer.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application using:
```bash
streamlit run main.py
```

## Deployment

The application is deployed on Azure App Service and automatically updates when changes are pushed to the main branch on GitHub.

## License

This project is open source and available under the MIT License. 