import os
from dotenv import load_dotenv
import httpx

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
        self.client = httpx.AsyncClient(
            base_url=PAYSTACK_API_BASE,
            headers={"Authorization": f"Bearer {self.api_key}"},
        )

    async def get_balance(self):
        """Get the balance from the Paystack API."""
        response = await self.client.get("/balance")
        return response.json()

    async def get_balance_ledger(self):
        """Get the balance ledger from the Paystack API."""
        response = await self.client.get("/balance/ledger")
        return response.json()

    async def list_customers(self):
        """List customers from the Paystack API."""
        response = await self.client.get("/customer")
        return response.json()

    async def create_customer(
        self, email: str, first_name: str, last_name: str, phone: str | None = None
    ):
        """Create a customer using the Paystack API."""
        payload = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
        }
        response = await self.client.post("/customer", json=payload)
        return response.json()

    async def fetch_customer(self, customer_code: str):
        """Fetch a customer's details from the Paystack API."""
        response = await self.client.get(f"/customer/{customer_code}")
        return response.json()

    async def update_customer(
        self, code: str, first_name: str, last_name: str, phone: str | None = None
    ):
        """Update a customer's details using the Paystack API."""
        payload = {"first_name": first_name, "last_name": last_name, "phone": phone}
        response = await self.client.put(f"/customer/{code}", json=payload)
        return response.json()

    async def list_products(self):
        """List products from the Paystack API."""
        response = await self.client.get("/product")
        return response.json()

    async def create_product(
        self, name: str, description: str, price: int, currency: str, quantity: int = 1
    ):
        """Create a product using the Paystack API."""
        payload = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
            "quantity": quantity,
        }
        response = await self.client.post("/product", json=payload)
        return response.json()

    async def fetch_product(self, product_code: str):
        """Fetch a product's details from the Paystack API."""
        response = await self.client.get(f"/product/{product_code}")
        return response.json()

    async def update_product(
        self,
        product_code: str,
        name: str | None,
        description: str | None,
        price: int | None,
        currency: str | None,
        quantity: int | None = None,
    ):
        """Update a product's details using the Paystack API."""
        payload = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
            "quantity": quantity,
        }
        response = await self.client.put(f"/product/{product_code}", json=payload)
        return response.json()

    async def delete_product(self, product_code: str):
        """Delete a product using the Paystack API."""
        response = await self.client.delete(f"/product/{product_code}")
        return response.json()

    async def list_invoices(self):
        """List invoices from the Paystack API."""
        response = await self.client.get("/paymentrequest")
        return response.json()

    async def create_invoice(self, customer: str, amount: int):
        """Create an invoice using the Paystack API."""
        payload = {"customer": customer, "amount": amount}
        response = await self.client.post("/paymentrequest", json=payload)
        return response.json()

    async def list_transactions(self):
        """List transactions from the Paystack API."""
        response = await self.client.get("/transaction")
        return response.json()

    async def initialize_transaction(self, email: str, amount: int, currency: str):
        """Initialize a transaction using the Paystack API."""
        payload = {"email": email, "amount": amount, "currency": currency}
        response = await self.client.post("/transaction/initialize", json=payload)
        return response.json()

    async def verify_transaction(self, reference: str):
        """Verify a transaction using the Paystack API."""
        response = await self.client.get(f"/transaction/verify/{reference}")
        return response.json()

    async def fetch_transaction(self, transaction_id: str):
        """Fetch a transaction's details from the Paystack API."""
        response = await self.client.get(f"/transaction/{transaction_id}")
        return response.json()

    async def get_transaction_timeline(self, id_or_reference: str):
        """Get a transaction's timeline from the Paystack API."""
        response = await self.client.get(f"/transaction/timeline/{id_or_reference}")
        return response.json()

    async def download_transactions(
        self,
        per_page: int | None = 50,
        page: int | None = 1,
        from_date: str | None = None,
        to_date: str | None = None,
    ):
        """Download a transactions receipt from the Paystack API."""
        params = {"perPage": per_page, "page": page, "from": from_date, "to": to_date}
        response = await self.client.get("/transaction/export", params=params)
        return response.json()

    async def create_refund(self, transaction: str, amount: int | None = None):
        """Create a refund using the Paystack API."""
        payload = {"transaction": transaction, "amount": amount}
        response = await self.client.post("/refund", json=payload)
        return response.json()

    async def list_subscriptions(self):
        """List subscriptions from the Paystack API."""
        response = await self.client.get("/subscription")
        return response.json()

    async def disable_subscription(self, code: str, token: str):
        """Disable a subscription using the Paystack API."""
        payload = {"code": code, "token": token}
        response = await self.client.post("/subscription/disable", json=payload)
        return response.json()

    async def list_disputes(self):
        """List disputes from the Paystack API."""
        response = await self.client.get("/dispute")
        return response.json()

    async def add_evidence_to_dispute(
        self,
        dispute_id: str,
        customer_email: str,
        customer_name: str,
        customer_phone: str,
        service_details: str,
    ):
        """Add evidence to a dispute using the Paystack API."""
        payload = {
            "customer_email": customer_email,
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "service_details": service_details,
        }
        response = await self.client.post(f"/dispute/{dispute_id}/evidence", json=payload)
        return response.json()

    async def fetch_dispute(self, dispute_id: str):
        """Fetch a dispute's details from the Paystack API."""
        response = await self.client.get(f"/dispute/{dispute_id}")
        return response.json()

    async def download_dispute(
        self,
        per_page: int | None = 50,
        page: int | None = 1,
        from_date: str | None = None,
        to_date: str | None = None,
    ):
        """Download a dispute receipt from the Paystack API."""
        params = {"perPage": per_page, "page": page, "from": from_date, "to": to_date}
        response = await self.client.get("/dispute/export", params=params)
        return response.json()

    async def resolve_dispute(
        self,
        dispute_id: str,
        resolution: str,
        message: str,
        refund_amount: str,
        uploaded_filename: str,
        evidence: str | None = None,
    ):
        """Resolve a dispute using the Paystack API."""
        payload = {
            "resolution": resolution,
            "message": message,
            "refund_amount": refund_amount,
            "uploaded_filename": uploaded_filename,
            "evidence": evidence,
        }
        response = await self.client.put(f"/dispute/{dispute_id}/resolve", json=payload)
        return response.json()

    async def create_payment_page(
        self, name: str, amount: int, description: str | None = None
    ):
        """Create a payment page using the Paystack API."""
        payload = {"name": name, "amount": amount, "description": description}
        response = await self.client.post("/page", json=payload)
        return response.json()

    async def list_payment_pages(self):
        """List payment pages from the Paystack API."""
        response = await self.client.get("/page")
        return response.json()

    async def fetch_payment_page(self, id: str):
        """Fetch a payment page's details from the Paystack API."""
        response = await self.client.get(f"/page/{id}")
        return response.json()

    async def update_payment_page(
        self,
        id: str,
        name: str | None = None,
        description: str | None = None,
        amount: int | None = None,
    ):
        """Update a payment page using the Paystack API."""
        payload = {"name": name, "description": description, "amount": amount}
        response = await self.client.put(f"/page/{id}", json=payload)
        return response.json()

    async def disable_payment_page(self, id: str):
        """Disable a payment page using the Paystack API."""
        payload = {"active": False}
        response = await self.client.put(f"/page/{id}", json=payload)
        return response.json()

    async def enable_payment_page(self, id: str):
        """Enable a payment page using the Paystack API."""
        payload = {"active": True}
        response = await self.client.put(f"/page/{id}", json=payload)
        return response.json()

    async def add_products_to_payment_page(self, id: str, products: list[str]):
        """Add products to a payment page using the Paystack API."""
        payload = {"product": products}
        response = await self.client.post(f"/page/{id}/product", json=payload)
        return response.json()

    async def create_plan(self, name: str, amount: int, interval: str):
        """Create a plan using the Paystack API."""
        payload = {"name": name, "amount": amount, "interval": interval}
        response = await self.client.post("/plan", json=payload)
        return response.json()

    async def list_plans(self):
        """List plans from the Paystack API."""
        response = await self.client.get("/plan")
        return response.json()

    async def fetch_plan(self, plan_code: str):
        """Fetch a plan's details from the Paystack API."""
        response = await self.client.get(f"/plan/{plan_code}")
        return response.json()

    async def resolve_account_number(self, account_number: str, bank_code: str):
        """Resolve an account number using the Paystack API."""
        params = {"account_number": account_number, "bank_code": bank_code}
        response = await self.client.get("/bank/resolve", params=params)
        return response.json()

    async def list_avs(
        self,
        country: str,
        type: str | None = None,
        currency: str | None = None,
    ):
        """List states for address_verification the Paystack API."""
        params = {"type": type, "country": country, "currency": currency}
        response = await self.client.get("/address_verification/states", params=params)
        return response.json()

    async def fetch_banks(
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
        params = {
            "country": country,
            "pay_with_bank_transfer": pay_with_bank_transfer,
            "use_cursor": use_cursor,
            "per_page": per_page,
            "next": next,
            "previous": previous,
            "gateway": gateway,
        }
        response = await self.client.get("/bank", params=params)
        return response.json()

    async def list_countries(self):
        """List countries from the Paystack API."""
        response = await self.client.get("/country")
        return response.json()

    async def resolve_card_bin(self, card_bin: str):
        """Resolve a card bin using the Paystack API."""
        response = await self.client.get(f"/decision/bin/{card_bin}")
        return response.json()


class _LazyPaystackClient:
    _instance = None

    def __getattr__(self, name):
        if self._instance is None:
            self._instance = PaystackClient()
        return getattr(self._instance, name)


# A single client instance to be used by the tools
paystack_client = _LazyPaystackClient()