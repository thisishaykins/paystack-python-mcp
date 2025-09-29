import os
import paystack
from dotenv import load_dotenv
from typing import Any

load_dotenv()

PAYSTACK_API_BASE = "https://api.paystack.co"


class PaystackClient:
    """A wrapper for the Paystack API"""

    def __init__(self, api_key: str | None = None):
        if api_key is None:
            api_key = os.environ.get("PAYSTACK_API_KEY")
        if api_key is None:
            raise ValueError("Paystack API key not provided.")

        self.api_key = api_key
        paystack.api_key = self.api_key

    def get_balance(self):
        """Get the balance from the Paystack API."""
        return paystack.Balance.fetch()

    def get_balance_ledger(self):
        """Get the balance ledger from the Paystack API."""
        return paystack.Balance.ledger()

    def list_customers(self):
        """List customers from the Paystack API."""
        return paystack.Customer.list()

    def create_customer(
        self, email: str, first_name: str, last_name: str, phone: str | None = None
    ):
        """Create a customer using the Paystack API."""
        return paystack.Customer.create(
            email=email, first_name=first_name, last_name=last_name, phone=phone
        )

    def fetch_customer(self, customer_code: str):
        """Fetch a customer's details from the Paystack API."""
        return paystack.Customer.fetch(customer_code)

    def update_customer(
        self, code: str, first_name: str, last_name: str, phone: str | None = None
    ):
        """Update a customer's details using the Paystack API."""
        return paystack.Customer.update(
            code=code, first_name=first_name, last_name=last_name, phone=phone
        )

    def list_products(self):
        """List products from the Paystack API."""
        return paystack.Product.list()

    def create_product(
        self, name: str, description: str, price: int, currency: str, quantity: int = 1
    ):
        """Create a product using the Paystack API."""
        return paystack.Product.create(
            name=name,
            description=description,
            price=price,
            currency=currency,
            quantity=quantity,
        )

    def fetch_product(self, product_code: str):
        """Fetch a product's details from the Paystack API."""
        return paystack.Product.fetch(product_code)

    def update_product(
        self,
        product_code: str,
        name: str | None,
        description: str | None,
        price: int | None,
        currency: str | None,
        quantity: int | None = None,
    ):
        """Update a product's details using the Paystack API."""
        return paystack.Product.update(
            id=product_code,
            name=name,
            description=description,
            price=price,
            currency=currency,
            quantity=quantity,
        )

    def delete_product(self, product_code: str):
        """Delete a product using the Paystack API."""
        return paystack.Product.delete(product_code)

    def list_invoices(self):
        """List invoices from the Paystack API."""
        return paystack.PaymentRequest.fetch()

    def create_invoice(self, customer: str, amount: int):
        """Create an invoice using the Paystack API."""
        return paystack.PaymentRequest.create(customer=customer, amount=amount)

    def list_transactions(self):
        """List transactions from the Paystack API."""
        return paystack.Transaction.list()

    def initialize_transaction(self, email: str, amount: int, currency: str):
        """Initialize a transaction using the Paystack API."""
        return paystack.Transaction.initialize(
            email=email, amount=amount, currency=currency
        )

    def verify_transaction(self, reference: str):
        """Verify a transaction using the Paystack API."""
        return paystack.Transaction.verify(reference=reference)

    def fetch_transaction(self, transaction_id: str):
        """Fetch a transaction's details from the Paystack API."""
        return paystack.Transaction.fetch(transaction_id)

    def get_transaction_timeline(self, id_or_reference: str):
        """Get a transaction's timeline from the Paystack API."""
        return paystack.Transaction.timeline(id_or_reference)

    def download_transactions(
        self,
        per_page: int | None = 50,
        page: int | None = 1,
        from_date: str | None = None,
        to_date: str | None = None,
    ):
        """Download a transactions receipt from the Paystack API."""
        return paystack.Transaction.download(
            per_page=per_page, page=page, _from=from_date, to=to_date
        )

    def create_refund(self, transaction: str, amount: int | None = None):
        """Create a refund using the Paystack API."""
        return paystack.Refund.create(transaction=transaction, amount=amount)

    def list_subscriptions(self):
        """List subscriptions from the Paystack API."""
        return paystack.Subscription.list()

    def disable_subscription(self, code: str, token: str):
        """Disable a subscription using the Paystack API."""
        return paystack.Subscription.disable(code=code, token=token)

    def list_disputes(self):
        """List disputes from the Paystack API."""
        return paystack.Dispute.list()

    def add_evidence_to_dispute(
        self,
        dispute_id: str,
        customer_email: str,
        customer_name: str,
        customer_phone: str,
        service_details: str,
    ):
        """Add evidence to a dispute using the Paystack API."""
        return paystack.Dispute.add_evidence(
            id=dispute_id,
            customer_email=customer_email,
            customer_name=customer_name,
            customer_phone=customer_phone,
            service_details=service_details,
        )

    def fetch_dispute(self, dispute_id: str):
        """Fetch a dispute's details from the Paystack API."""
        return paystack.Dispute.fetch(dispute_id)

    def download_dispute(
        self,
        per_page: int | None = 50,
        page: int | None = 1,
        from_date: str | None = None,
        to_date: str | None = None,
    ):
        """Download a dispute receipt from the Paystack API."""
        return paystack.Dispute.download(
            per_page=per_page, page=page, _from=from_date, to=to_date
        )

    def resolve_dispute(
        self,
        dispute_id: str,
        resolution: str,
        message: str,
        refund_amount: str,
        uploaded_filename: str,
        evidence: str | None = None,
    ):
        """Resolve a dispute using the Paystack API."""
        return paystack.Dispute.resolve(
            dispute_id, resolution, message, refund_amount, uploaded_filename, evidence
        )

    def create_payment_page(
        self, name: str, amount: int, description: str | None = None
    ):
        """Create a payment page using the Paystack API."""
        return paystack.Page.create(name=name, amount=amount, description=description)

    def list_payment_pages(self):
        """List payment pages from the Paystack API."""
        return paystack.Page.list()

    def fetch_payment_page(self, id: str):
        """Fetch a payment page's details from the Paystack API."""
        return paystack.Page.fetch(id)

    def update_payment_page(
        self,
        id: str,
        name: str | None = None,
        description: str | None = None,
        amount: int | None = None,
    ):
        """Update a payment page using the Paystack API."""
        return paystack.Page.update(
            id, name=name, description=description, amount=amount
        )

    def disable_payment_page(self, id: str):
        """Disable a payment page using the Paystack API."""
        return paystack.Page.update(id, active=False)

    def enable_payment_page(self, id: str):
        """Enable a payment page using the Paystack API."""
        return paystack.Page.update(id, active=True)

    def add_products_to_payment_page(self, id: str, products: list[str]):
        """Add products to a payment page using the Paystack API."""
        return paystack.Page.add_products(id=id, products=products)

    def create_plan(self, name: str, amount: int, interval: str):
        """Create a plan using the Paystack API."""
        return paystack.Plan.create(name=name, amount=amount, interval=interval)

    def list_plans(self):
        """List plans from the Paystack API."""
        return paystack.Plan.list()

    def fetch_plan(self, plan_code: str):
        """Fetch a plan's details from the Paystack API."""
        return paystack.Plan.fetch(plan_code)

    def resolve_account_number(self, account_number: str, bank_code: str):
        """Resolve an account number using the Paystack API."""
        return paystack.Verification.resolve_account_number(
            account_number=account_number, bank_code=bank_code
        )

    def list_avs(
        self,
        type: str | None = None,
        country: str | None = None,
        currency: str | None = None,
    ):
        """List states for address_verification the Paystack API."""
        return paystack.Verification.avs(type=type, country=country, currency=currency)

    def fetch_banks(
        self,
        country: str | None = None,
        pay_with_bank_transfer: bool | None = None,
        use_cursor: bool | None = None,
        per_page: int | None = None,
        next: str | None = None,
        previous: str | None = None,
        gateway: str | None = None,
    ):
        """Fetch a bank's details from the Paystack API."""
        return paystack.Verification.fetch_banks(
            country=country,
            pay_with_bank_transfer=pay_with_bank_transfer,
            use_cursor=use_cursor,
            per_page=per_page,
            next=next,
            previous=previous,
            gateway=gateway,
        )

    def list_countries(self):
        """List countries from the Paystack API."""
        return paystack.Verification.list_countries()

    def resolve_card_bin(self, card_bin: str):
        """Resolve a card bin using the Paystack API."""
        return paystack.Verification.resolve_card_bin(card_bin)


# A single client instance to be used by the tools
paystack_client = PaystackClient()