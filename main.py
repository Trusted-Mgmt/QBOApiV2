import argparse
from qb_automation.actions import create_invoice, create_journal_entry, create_bill, create_deposit, create_check

def main():
    parser = argparse.ArgumentParser(description='QuickBooks Online Automation Framework')
    parser.add_argument('company_id', help='The company ID')
    parser.add_argument('action', help='The action to perform',
                        choices=['create_invoice', 'create_journal_entry', 'create_bill', 'create_deposit', 'create_check'])
    parser.add_argument('data_path', help='The path to the data file (JSON format)')

    args = parser.parse_args()

    if args.action == 'create_invoice':
        create_invoice.create_invoice(args.company_id, args.data_path)
    elif args.action == 'create_journal_entry':
        create_journal_entry.create_journal_entry(args.company_id, args.data_path)
    elif args.action == 'create_bill':
        create_bill.create_bill(args.company_id, args.data_path)
    elif args.action == 'create_deposit':
        create_deposit.create_deposit(args.company_id, args.data_path)
    elif args.action == 'create_check':
        create_check.create_check(args.company_id, args.data_path)

if __name__ == '__main__':
    main()
