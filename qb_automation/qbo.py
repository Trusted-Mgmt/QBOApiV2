from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
from quickbooks.client import QuickBooks
from quickbooks.objects.invoice import Invoice
from quickbooks.objects.journalentry import JournalEntry
from quickbooks.objects.bill import Bill
from quickbooks.objects.deposit import Deposit
from quickbooks.objects.check import Check
from quickbooks.objects.payment import Payment

from .auth.qbo_auth import QBOAuth

class QBO:
    def __init__(self, company_id):
        self.auth_client = QBOAuth(company_id).get_access_token()
        self.client = QuickBooks(
            auth_client=self.auth_client,
            refresh_token=self.auth_client.refresh_token,
            company_id=self.auth_client.realm_id,
        )

    def create_invoice(self, invoice_data):
        invoice = Invoice.from_json(invoice_data)
        return invoice.save(qb=self.client)

    def create_journal_entry(self, journal_entry_data):
        journal_entry = JournalEntry.from_json(journal_entry_data)
        return journal_entry.save(qb=self.client)

    def create_bill(self, bill_data):
        bill = Bill.from_json(bill_data)
        return bill.save(qb=self.client)

    def create_deposit(self, deposit_data):
        deposit = Deposit.from_json(deposit_data)
        return deposit.save(qb=self.client)

    def create_check(self, check_data):
        check = Check.from_json(check_data)
        return check.save(qb=self.client)

    def create_payment(self, payment_data):
        payment = Payment.from_json(payment_data)
        return payment.save(qb=self.client)

    def get_report(self, report_type, report_date):
        # This is a placeholder for the report generation logic
        pass
