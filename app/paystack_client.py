import os
import paystack
from dotenv import load_dotenv
import httpx
from typing import Any

load_dotenv()

PAYSTACK_API_BASE = "https://api.paystack.co"

async def paystack_post_request(endpoint: str, headers: dict[str, str], data: dict[str, Any]) -> dict[str, Any] | None:
    """Make a POST request to the Paystack API with proper error handling."""
    url = f"{PAYSTACK_API_BASE}/{endpoint}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=data, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

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
        return paystack.Balance.get_balance()

    def list_customers(self):
        """List customers from the Paystack API."""
        return paystack.Customer.list()

    def create_customer(self, email: str, first_name: str, last_name: str):
        """Create a customer using the Paystack API."""
        return paystack.Customer.create(email=email, first_name=first_name, last_name=last_name)

    def list_products(self):
        """List products from the Paystack API."""
        return paystack.Product.list()

    def create_product(self, name: str, description: str, price: int, currency: str):
        """Create a product using the Paystack API."""
        return paystack.Product.create(name=name, description=description, price=price, currency=currency)

    def list_prices(self):
        """List prices from the Paystack API."""
        return paystack.Price.list()

    def create_price(self, currency: str, amount: int, name: str):
        """Create a price using the Paystack API."""
        return paystack.Price.create(currency=currency, amount=amount, name=name)

    def list_invoices(self):
        """List invoices from the Paystack API."""
        return paystack.Invoice.list()

    def create_invoice(self, customer: str, amount: int):
        """Create an invoice using the Paystack API."""
        return paystack.Invoice.create(customer=customer, amount=amount)

    def list_transactions(self):
        """List transactions from the Paystack API."""
        return paystack.Transaction.list()

    def create_refund(self, transaction: str, amount: int | None = None):
        """Create a refund using the Paystack API."""
        return paystack.Refund.create(transaction=transaction, amount=amount)

    def list_subscriptions(self):
        """List subscriptions from the Paystack API."""
        return paystack.Subscription.list()

    def disable_subscription(self, code: str, token: str):
        """Disable a subscription using the Paystack API."""
        return paystack.Subscription.disable(code=code, token=token)

    def list_coupons(self):
        """List coupons from the Paystack API."""
        return paystack.Coupon.list()

    def create_coupon(self, coupon: str, amount_off: int):
        """Create a coupon using the Paystack API."""
        return paystack.Coupon.create(coupon=coupon, amount_off=amount_off)

    def list_disputes(self):
        """List disputes from the Paystack API."""
        return paystack.Dispute.list()

    async def add_evidence_to_dispute(self, dispute_id: str, customer_email: str, customer_name: str, customer_phone: str, service_details: str):
        """Add evidence to a dispute using the Paystack API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "customer_email": customer_email,
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "service_details": service_details,
        }
        endpoint = f"dispute/{dispute_id}/evidence"
        return await paystack_post_request(endpoint, headers, data)

    def create_payment_page(self, name: str, amount: int):
        """Create a payment page using the Paystack API."""
        return paystack.Page.create(name=name, amount=amount)

# A single client instance to be used by the tools
paystack_client = PaystackClient()