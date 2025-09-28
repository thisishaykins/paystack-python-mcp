from app.server import mcp
from app.paystack_client import paystack_client

@mcp.tool(name="balance.read")
def get_balance():
    """
    Retrieves the balance from a Paystack account.
    """
    return paystack_client.get_balance()


@mcp.tool(name="customer.list")
def list_customers():
    """
    Retrieves a list of all customers.
    """
    return paystack_client.list_customers()


@mcp.tool(name="customer.create")
def create_customer(email: str, first_name: str, last_name: str):
    """
    Creates a new customer.

    Args:
        email: The customer's email address.
        first_name: The customer's first name.
        last_name: The customer's last name.
    """
    return paystack_client.create_customer(email, first_name, last_name)


@mcp.tool(name="customer.read")
def fetch_customer(customer_code: str):
    """
    Fetches the details of a specific customer.

    Args:
        customer_code: The code of the customer to fetch.
    """
    return paystack_client.fetch_customer(customer_code)


@mcp.tool(name="customer.update")
def update_customer(code: str, first_name: str, last_name: str):
    """
    Updates the details of a specific customer.

    Args:
        code: The code of the customer to update.
        first_name: The customer's new first name.
        last_name: The customer's new last name.
    """
    return paystack_client.update_customer(code, first_name, last_name)


@mcp.tool(name="product.list")
def list_products():
    """
    Retrieves a list of all products.
    """
    return paystack_client.list_products()


@mcp.tool(name="product.create")
def create_product(name: str, description: str, price: int, currency: str):
    """
    Creates a new product.

    Args:
        name: The name of the product.
        description: A description of the product.
        price: The price of the product in the smallest currency unit (e.g., kobo).
        currency: The currency of the price (e.g., NGN).
    """
    return paystack_client.create_product(name, description, price, currency)


@mcp.tool(name="price.list")
def list_prices():
    """
    Retrieves a list of all prices.
    """
    return paystack_client.list_prices()


@mcp.tool(name="price.create")
def create_price(currency: str, amount: int, name: str):
    """
    Creates a new price.

    Args:
        currency: The currency of the price (e.g., NGN).
        amount: The amount of the price in the smallest currency unit (e.g., kobo).
        name: The name of the price.
    """
    return paystack_client.create_price(currency, amount, name)


@mcp.tool(name="invoice.list")
def list_invoices():
    """
    Retrieves a list of all invoices.
    """
    return paystack_client.list_invoices()


@mcp.tool(name="invoice.create")
def create_invoice(customer: str, amount: int):
    """
    Creates a new invoice.

    Args:
        customer: The customer's code or email address.
        amount: The amount of the invoice in the smallest currency unit (e.g., kobo).
    """
    return paystack_client.create_invoice(customer, amount)


@mcp.tool(name="transaction.list")
def list_transactions():
    """
    Retrieves a list of all transactions.
    """
    return paystack_client.list_transactions()


@mcp.tool(name="transaction.initialize")
def initialize_transaction(email: str, amount: int, currency: str):
    """
    Initializes a new transaction.

    Args:
        email: The customer's email address.
        amount: The amount of the transaction in the smallest currency unit (e.g., kobo).
        currency: The currency of the transaction (e.g., NGN).
    """
    return paystack_client.initialize_transaction(email, amount, currency)


@mcp.tool(name="transaction.verify")
def verify_transaction(reference: str):
    """
    Verifies the status of a transaction.

    Args:
        reference: The reference of the transaction to verify.
    """
    return paystack_client.verify_transaction(reference)


@mcp.tool(name="transaction.read")
def fetch_transaction(transaction_id: int):
    """
    Fetches the details of a specific transaction.

    Args:
        transaction_id: The ID of the transaction to fetch.
    """
    return paystack_client.fetch_transaction(transaction_id)


@mcp.tool(name="refund.create")
def create_refund(transaction: str, amount: int | None = None):
    """
    Creates a new refund.

    Args:
        transaction: The transaction reference or ID to refund.
        amount: The amount to refund in the smallest currency unit (e.g., kobo).
                If not provided, a full refund will be issued.
    """
    return paystack_client.create_refund(transaction, amount)


@mcp.tool(name="subscription.list")
def list_subscriptions():
    """
    Retrieves a list of all subscriptions.
    """
    return paystack_client.list_subscriptions()


@mcp.tool(name="subscription.disable")
def disable_subscription(code: str, token: str):
    """
    Disables a subscription.

    Args:
        code: The subscription code.
        token: The email token of the customer.
    """
    return paystack_client.disable_subscription(code, token)


@mcp.tool(name="coupon.list")
def list_coupons():
    """
    Retrieves a list of all coupons.
    """
    return paystack_client.list_coupons()


@mcp.tool(name="coupon.create")
def create_coupon(coupon: str, amount_off: int):
    """
    Creates a new coupon.

    Args:
        coupon: The name of the coupon.
        amount_off: The amount off the price in the smallest currency unit (e.g., kobo).
    """
    return paystack_client.create_coupon(coupon, amount_off)


@mcp.tool(name="dispute.list")
def list_disputes():
    """
    Retrieves a list of all disputes.
    """
    return paystack_client.list_disputes()


@mcp.tool(name="dispute.add_evidence")
async def add_evidence_to_dispute(dispute_id: str, customer_email: str, customer_name: str, customer_phone: str, service_details: str):
    """
    Adds evidence to a dispute.

    Args:
        dispute_id: The ID of the dispute.
        customer_email: The email address of the customer.
        customer_name: The name of the customer.
        customer_phone: The phone number of the customer.
        service_details: Details of the service provided.
    """
    return await paystack_client.add_evidence_to_dispute(dispute_id, customer_email, customer_name, customer_phone, service_details)


@mcp.tool(name="payment_page.create")
def create_payment_page(name: str, amount: int):
    """
    Creates a new payment page.

    Args:
        name: The name of the payment page.
        amount: The amount for the payment page in the smallest currency unit (e.g., kobo).
    """
    return paystack_client.create_payment_page(name, amount)


@mcp.tool(name="plan.create")
def create_plan(name: str, amount: int, interval: str):
    """
    Creates a new subscription plan.

    Args:
        name: The name of the plan.
        amount: The amount for the plan in the smallest currency unit (e.g., kobo).
        interval: The frequency of the plan (e.g., 'daily', 'weekly', 'monthly').
    """
    return paystack_client.create_plan(name, amount, interval)


@mcp.tool(name="plan.list")
def list_plans():
    """
    Retrieves a list of all subscription plans.
    """
    return paystack_client.list_plans()


@mcp.tool(name="plan.read")
def fetch_plan(plan_code: str):
    """
    Fetches the details of a specific subscription plan.

    Args:
        plan_code: The code of the plan to fetch.
    """
    return paystack_client.fetch_plan(plan_code)


@mcp.tool(name="verification.resolve_account_number")
def resolve_account_number(account_number: str, bank_code: str):
    """
    Resolves an account number to get the account holder's name.

    Args:
        account_number: The account number to resolve.
        bank_code: The bank code of the account's bank.
    """
    return paystack_client.resolve_account_number(account_number, bank_code)