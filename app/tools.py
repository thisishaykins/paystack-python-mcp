from app.server import mcp
from app.paystack_client import paystack_client

@mcp.tool()
def get_balance():
    """
    Retrieves the balance from a Paystack account.
    """
    return paystack_client.get_balance()


@mcp.tool()
def list_customers():
    """
    Retrieves a list of all customers.
    """
    return paystack_client.list_customers()


@mcp.tool()
def create_customer(email: str, first_name: str, last_name: str):
    """
    Creates a new customer.

    Args:
        email: The customer's email address.
        first_name: The customer's first name.
        last_name: The customer's last name.
    """
    return paystack_client.create_customer(email, first_name, last_name)


@mcp.tool()
def list_products():
    """
    Retrieves a list of all products.
    """
    return paystack_client.list_products()


@mcp.tool()
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


@mcp.tool()
def list_prices():
    """
    Retrieves a list of all prices.
    """
    return paystack_client.list_prices()


@mcp.tool()
def create_price(currency: str, amount: int, name: str):
    """
    Creates a new price.

    Args:
        currency: The currency of the price (e.g., NGN).
        amount: The amount of the price in the smallest currency unit (e.g., kobo).
        name: The name of the price.
    """
    return paystack_client.create_price(currency, amount, name)


@mcp.tool()
def list_invoices():
    """
    Retrieves a list of all invoices.
    """
    return paystack_client.list_invoices()


@mcp.tool()
def create_invoice(customer: str, amount: int):
    """
    Creates a new invoice.

    Args:
        customer: The customer's code or email address.
        amount: The amount of the invoice in the smallest currency unit (e.g., kobo).
    """
    return paystack_client.create_invoice(customer, amount)


@mcp.tool()
def list_transactions():
    """
    Retrieves a list of all transactions.
    """
    return paystack_client.list_transactions()


@mcp.tool()
def create_refund(transaction: str, amount: int | None = None):
    """
    Creates a new refund.

    Args:
        transaction: The transaction reference or ID to refund.
        amount: The amount to refund in the smallest currency unit (e.g., kobo).
                If not provided, a full refund will be issued.
    """
    return paystack_client.create_refund(transaction, amount)


@mcp.tool()
def list_subscriptions():
    """
    Retrieves a list of all subscriptions.
    """
    return paystack_client.list_subscriptions()


@mcp.tool()
def disable_subscription(code: str, token: str):
    """
    Disables a subscription.

    Args:
        code: The subscription code.
        token: The email token of the customer.
    """
    return paystack_client.disable_subscription(code, token)


@mcp.tool()
def list_coupons():
    """
    Retrieves a list of all coupons.
    """
    return paystack_client.list_coupons()


@mcp.tool()
def create_coupon(coupon: str, amount_off: int):
    """
    Creates a new coupon.

    Args:
        coupon: The name of the coupon.
        amount_off: The amount off the price in the smallest currency unit (e.g., kobo).
    """
    return paystack_client.create_coupon(coupon, amount_off)


@mcp.tool()
def list_disputes():
    """
    Retrieves a list of all disputes.
    """
    return paystack_client.list_disputes()


@mcp.tool()
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


@mcp.tool()
def create_payment_page(name: str, amount: int):
    """
    Creates a new payment page.

    Args:
        name: The name of the payment page.
        amount: The amount for the payment page in the smallest currency unit (e.g., kobo).
    """
    return paystack_client.create_payment_page(name, amount)