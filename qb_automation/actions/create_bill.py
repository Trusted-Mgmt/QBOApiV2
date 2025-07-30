import json
from qb_automation.qbo import QBO

def create_bill(company_id, bill_data_path):
    with open(bill_data_path) as f:
        bill_data = json.load(f)

    qbo = QBO(company_id)
    bill = qbo.create_bill(bill_data)
    print(f"Bill created with ID: {bill.Id}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('company_id', help='The company ID')
    parser.add_argument('bill_data_path', help='The path to the bill data file')
    args = parser.parse_args()

    create_bill(args.company_id, args.bill_data_path)
