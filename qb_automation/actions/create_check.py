import json
from qb_automation.qbo import QBO

def create_check(company_id, check_data_path):
    with open(check_data_path) as f:
        check_data = json.load(f)

    qbo = QBO(company_id)
    check = qbo.create_check(check_data)
    print(f"Check created with ID: {check.Id}")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('company_id', help='The company ID')
    parser.add_argument('check_data_path', help='The path to the check data file')
    args = parser.parse_args()

    create_check(args.company_id, args.check_data_path)
