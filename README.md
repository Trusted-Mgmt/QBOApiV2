# Python-based Automation Framework for QuickBooks Online

This framework provides a set of tools to automate interactions with QuickBooks Online for multiple companies. It allows you to perform actions such as posting deposits, invoices, journal entries, bills/expenses/checks, and pulling reports.

## Features

- **Multi-company support:** Each company has its own authentication token, ensuring secure and separate access.
- **Modular design:** Each action is a separately callable module, making it easy to extend and maintain.
- **Command-line interface:** The main runner accepts command-line arguments to specify the action and company.
- **Google Sheets integration:** Define mapping templates in Google Sheets for easy data management.
- **Google Drive and Gmail integration:** Pull reports from either Gmail attachments or Google Drive.

## Directory Structure

```
.
├── config
│   ├── qbo_credentials.json
│   ├── google_credentials.json
│   └── tokens
│       ├── company1_token.json
│       └── company2_token.json
├── qb_automation
│   ├── actions
│   │   ├── create_bill.py
│   │   ├── create_check.py
│   │   ├── create_deposit.py
│   │   ├── create_invoice.py
│   │   └── create_journal_entry.py
│   ├── auth
│   │   └── qbo_auth.py
│   ├── google
│   │   ├── drive.py
│   │   └── sheets.py
│   ├── __init__.py
│   └── qbo.py
├── templates
│   └── mapping_template.csv
├── main.py
├── requirements.txt
└── README.md
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/qbo-automation.git
   cd qbo-automation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure QuickBooks Online API credentials:**
   - Create a `config/qbo_credentials.json` file with your QuickBooks Online API credentials. See `config/qbo_credentials.json.template` for a template.

4. **Configure Google API credentials:**
   - Create a `config/google_credentials.json` file with your Google API credentials. See `config/google_credentials.json.template` for a template.

5. **Authenticate with QuickBooks Online:**
   - Run the `qb_automation/auth/qbo_auth.py` script to authenticate with QuickBooks Online and generate a token file for each company.
   ```bash
   python -m qb_automation.auth.qbo_auth
   ```

6. **Authenticate with Google:**
   - The first time you run a script that uses the Google Drive or Google Sheets API, you will be prompted to authenticate with Google. A `config/tokens/google_token.json` file will be created to store your credentials.

## Usage

To run an action, use the `main.py` script with the following command-line arguments:

```bash
python main.py <company_id> <action> <data_path>
```

- `company_id`: The ID of the company to perform the action on.
- `action`: The action to perform.
- `data_path`: The path to the data file (in JSON format).

**Example:**

```bash
python main.py 123456789 create_invoice /path/to/invoice_data.json
```

## Available Actions

- `create_invoice`: Create a new invoice.
- `create_journal_entry`: Create a new journal entry.
- `create_bill`: Create a new bill.
- `create_deposit`: Create a new deposit.
- `create_check`: Create a new check.

## Disclaimer

This is a basic framework and may need to be adapted to your specific needs. Please use it at your own risk.
