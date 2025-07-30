import json
from qb_automation.qbo import QBO

def create_invoice(company_id, invoice_data_path):
    with open(invoice_data_path) as f:
        invoice_data = json.load(f)

    qbo = QBO(company_id)
    invoice = qbo.create_invoice(invoice_data)
    print(f"Invoice created with ID: {invoice.Id}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('company_id', help='The company ID')
    parser.add_argument('invoice_data_path', help='The path to the invoice data file')
    args = parser.parse_args()

    create_invoice(args.company_id, args.invoice_data_path)
