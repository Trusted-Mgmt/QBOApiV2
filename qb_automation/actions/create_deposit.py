import json
from qb_automation.qbo import QBO

def create_deposit(company_id, deposit_data_path):
    with open(deposit_data_path) as f:
        deposit_data = json.load(f)

    qbo = QBO(company_id)
    deposit = qbo.create_deposit(deposit_data)
    print(f"Deposit created with ID: {deposit.Id}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('company_id', help='The company ID')
    parser.add_argument('deposit_data_path', help='The path to the deposit data file')
    args = parser.parse_args()

    create_deposit(args.company_id, args.deposit_data_path)
