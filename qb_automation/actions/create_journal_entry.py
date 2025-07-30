import json
from qb_automation.qbo import QBO

def create_journal_entry(company_id, journal_entry_data_path):
    with open(journal_entry_data_path) as f:
        journal_entry_data = json.load(f)

    qbo = QBO(company_id)
    journal_entry = qbo.create_journal_entry(journal_entry_data)
    print(f"Journal entry created with ID: {journal_entry.Id}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('company_id', help='The company ID')
    parser.add_argument('journal_entry_data_path', help='The path to the journal entry data file')
    args = parser.parse_args()

    create_journal_entry(args.company_id, args.journal_entry_data_path)
