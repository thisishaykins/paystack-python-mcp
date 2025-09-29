from app.server import mcp
from app.paystack_client import paystack_client


@mcp.tool(name="balance.read")
def get_balance():
    """
    Retrieves the balance from a Paystack account.
    """
    return paystack_client.get_balance()


@mcp.tool(name="balance.ledger")
def get_balance_ledger():
    """
    Retrieves the balance ledger from a Paystack account.
    """
    return paystack_client.get_balance_ledger()


@mcp.tool(name="customer.list")
def list_customers():
    """
    Retrieves a list of all customers.
    """
    return paystack_client.list_customers()


@mcp.tool(name="customer.create")
def create_customer(
    email: str, first_name: str, last_name: str, phone: str | None = None
):
    """
    Creates a new customer.

    Args:
        email: The customer's email address.
        first_name: The customer's first name.
        last_name: The customer's last name.
        phone: The customer's phone number (optional).
    """
    return paystack_client.create_customer(email, first_name, last_name, phone)


@mcp.tool(name="customer.read")
def fetch_customer(customer_code: str):
    """
    Fetches the details of a specific customer.

    Args:
        customer_code: The code of the customer to fetch.
    """
    return paystack_client.fetch_customer(customer_code)


@mcp.tool(name="customer.update")
def update_customer(
    code: str, first_name: str, last_name: str, phone: str | None = None
):
    """
    Updates the details of a specific customer.

    Args:
        code: The code of the customer to update.
        first_name: The customer's new first name.
        last_name: The customer's new last name.
        phone: The customer's new phone number (optional).
    """
    return paystack_client.update_customer(code, first_name, last_name, phone)


@mcp.tool(name="product.list")
def list_products():
    """
    Retrieves a list of all products.
    """
    return paystack_client.list_products()


@mcp.tool(name="product.create")
def create_product(
    name: str, description: str, price: int, currency: str, quantity: int = 1
):
    """
    Creates a new product.

    Args:
        name: The name of the product.
        description: A description of the product.
        price: The price of the product in the smallest currency unit (e.g., kobo).
        currency: The currency of the price (e.g., NGN).
        quantity: The available quantity of the product (default is 1).
    """
    return paystack_client.create_product(name, description, price, currency, quantity)


@mcp.tool(name="product.read")
def fetch_product(product_code: str):
    """
    Fetches the details of a specific product.

    Args:
        product_code: The code of the product to fetch.
    """
    return paystack_client.fetch_product(product_code)


@mcp.tool(name="product.update")
def update_product(
    product_code: str,
    name: str | None = None,
    description: str | None = None,
    price: int | None = None,
    currency: str | None = None,
    quantity: int | None = None,
):
    """
    Updates the details of a specific product.
    Args:
        product_code: The code of the product to update.
        name: The new name of the product (optional).
        description: The new description of the product (optional).
        price: The new price of the product in the smallest currency unit (e.g., kobo) (optional).
        currency: The new currency of the price (e.g., NGN) (optional).
        quantity: The new available quantity of the product (optional).
    """
    return paystack_client.update_product(
        product_code, name, description, price, currency, quantity
    )


@mcp.tool(name="product.delete")
def delete_product(product_code: str):
    """
    Deletes a specific product.
    Args:
        product_code: The code of the product to delete.
    """
    return paystack_client.delete_product(product_code)


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
def fetch_transaction(transaction_id: str):
    """
    Fetches the details of a specific transaction.

    Args:
        transaction_id: The ID of the transaction to fetch.
    """
    return paystack_client.fetch_transaction(transaction_id)


@mcp.tool(name="transaction.timeline")
def get_transaction_timeline(transaction_id_or_reference: str):
    """
    Retrieves the timeline of a specific transaction.

    Args:
        transaction_id_or_reference: The ID/Reference of the transaction to get the timeline for.
    """
    return paystack_client.get_transaction_timeline(transaction_id_or_reference)


@mcp.tool(name="transaction.download")
def download_transactions(
    per_page: int | None = 50,
    page: int | None = 1,
    from_date: str | None = None,
    to_date: str | None = None,
):
    """
    Downloads a list of transactions with optional filters.

    Args:
        per_page: Number of records to fetch per page (default is 50).
        page: The page number to retrieve (default is 1).
        from_date: The start date for filtering transactions (optional, format: 'YYYY-MM-DD').
        to_date: The end date for filtering transactions (optional, format: 'YYYY-MM-DD').
    """
    return paystack_client.download_transactions(per_page, page, from_date, to_date)


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


@mcp.tool(name="dispute.list")
def list_disputes():
    """
    Retrieves a list of all disputes.
    """
    return paystack_client.list_disputes()


@mcp.tool(name="dispute.read")
def fetch_dispute(dispute_id: str):
    """
    Fetches the details of a specific dispute.

    Args:
        dispute_id: The ID of the dispute to fetch.
    """
    return paystack_client.fetch_dispute(dispute_id)


@mcp.tool(name="dispute.download")
def download_dispute(
    per_page: int | None = 50,
    page: int | None = 1,
    from_date: str | None = None,
    to_date: str | None = None,
):
    """
    Downloads a list of dispute with optional filters.

    Args:
        per_page: Number of records to fetch per page (default is 50).
        page: The page number to retrieve (default is 1).
        from_date: The start date for filtering dispute (optional, format: 'YYYY-MM-DD').
        to_date: The end date for filtering dispute (optional, format: 'YYYY-MM-DD').
    """
    return paystack_client.download_dispute(per_page, page, from_date, to_date)


@mcp.tool(name="dispute.resolve")
def resolve_dispute(
    dispute_id: str,
    resolution: str,
    message: str,
    refund_amount: str,
    uploaded_filename: str,
    evidence: str | None = None,
):
    """
    Resolves a dispute.

    Args:
        dispute_id: 'id_example' # str | Dispute ID
        resolution: 'resolution_example' # str | Dispute resolution. Accepted values, merchant-accepted, declined
        message: 'message_example' # str | Reason for resolving
        refund_amount: 'refund_amount_example' # str | The amount to refund, in kobo if currency is NGN, pesewas, if currency is GHS, and cents, if currency is ZAR
        uploaded_filename: 'uploaded_filename_example' # str | Filename of attachment returned via response from the Dispute upload URL
        evidence: 'evidence_example' # str | Evidence Id for fraud claims (optional)

    """
    return paystack_client.resolve_dispute(
        dispute_id, resolution, message, refund_amount, uploaded_filename, evidence
    )


@mcp.tool(name="dispute.add_evidence")
def add_evidence_to_dispute(
    dispute_id: str,
    customer_email: str,
    customer_name: str,
    customer_phone: str,
    service_details: str,
):
    """
    Adds evidence to a dispute.

    Args:
        dispute_id: The ID of the dispute.
        customer_email: The email address of the customer.
        customer_name: The name of the customer.
        customer_phone: The phone number of the customer.
        service_details: Details of the service provided.
    """
    return paystack_client.add_evidence_to_dispute(
        dispute_id, customer_email, customer_name, customer_phone, service_details
    )


@mcp.tool(name="payment_page.create")
def create_payment_page(name: str, amount: int):
    """
    Creates a new payment page.

    Args:
        name: The name of the payment page.
        amount: The amount for the payment page in the smallest currency unit (e.g., kobo).
    """
    return paystack_client.create_payment_page(name, amount)


@mcp.tool(name="payment_page.list")
def list_payment_pages():
    """
    Retrieves a list of all payment pages.
    """
    return paystack_client.list_payment_pages()


@mcp.tool(name="payment_page.read")
def fetch_payment_page(id: str):
    """
    Fetches the details of a specific payment page.

    Args:
        id: The id of the payment page to fetch.
    """
    return paystack_client.fetch_payment_page(id)


@mcp.tool(name="payment_page.update")
def update_payment_page(
    id: str,
    name: str | None = None,
    description: str | None = None,
    amount: int | None = None,
):
    """
    Updates the details of a specific payment page.
    Args:
        id: The id of the payment page to update.
        name: The new name of the payment page (optional).
        description: The new description of the payment page (optional).
        amount: The new amount for the payment page in the smallest currency unit (e.g., kobo) (optional).
    """
    return paystack_client.update_payment_page(id, name, description, amount)


@mcp.tool(name="payment_page.disable")
def disable_payment_page(id: str):
    """
    Disables a specific payment page.
    Args:
        id: The id of the payment page to disable.
    """
    return paystack_client.disable_payment_page(id)


@mcp.tool(name="payment_page.enable")
def enable_payment_page(id: str):
    """
    Enables a specific payment page.
    Args:
        id: The id of the payment page to enable.
    """
    return paystack_client.enable_payment_page(id)


@mcp.tool(name="payment_page.add_products")
def add_products_to_payment_page(id: str, products: list[str]):
    """
    Adds products to a specific payment page.
    Args:
        id: The id of the payment page to add products to.
        products: A list of product codes to add to the payment page.
    """
    return paystack_client.add_products_to_payment_page(id, products)


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


@mcp.tool(name="verification.fetch_banks")
def fetch_banks(
    country: str | None = None,
    pay_with_bank_transfer: bool | None = None,
    use_cursor: bool | None = None,
    per_page: int | None = None,
    next: str | None = None,
    previous: str | None = None,
    gateway: str | None = None,
):
    """
    Fetches a list of banks.

    Args:
        country: The country code to filter banks by (optional).
        pay_with_bank_transfer: Filter banks that support bank transfer (optional).
        use_cursor: Whether to use cursor-based pagination (optional).
        per_page: Number of records to fetch per page (optional).
        next: The cursor for the next page (optional).
        previous: The cursor for the previous page (optional).
        gateway: Filter banks by payment gateway (optional).
    """
    return paystack_client.fetch_banks(
        country, pay_with_bank_transfer, use_cursor, per_page, next, previous, gateway
    )


@mcp.tool(name="verification.list_avs")
def list_avs(
    type: str | None = None, country: str | None = None, currency: str | None = None
):
    """
    Lists all available account verification services.
    Args:
        type: The type of verification service to filter by (optional).
        country: The country code to filter by (optional).
        currency: The currency code to filter by (optional).
    """
    return paystack_client.list_avs(type, country, currency)


@mcp.tool(name="verification.list_countries")
def list_countries():
    """
    Retrieves a list of all countries.
    """
    return paystack_client.list_countries()


@mcp.tool(name="verification.resolve_account_number")
def resolve_account_number(account_number: str, bank_code: str):
    """
    Resolves an account number to get the account holder's name.

    Args:
        account_number: The account number to resolve.
        bank_code: The bank code of the account's bank.
    """
    return paystack_client.resolve_account_number(account_number, bank_code)


@mcp.tool(name="verification.resolve_bvn")
def resolve_bvn(bvn: str):
    """
    Resolves a BVN to get the associated account details.

    Args:
        bvn: The BVN to resolve.
    """
    return paystack_client.resolve_bvn(bvn)


@mcp.tool(name="verification.resolve_card_bin")
def resolve_card_bin(card_bin: str):
    """
    Resolves a card BIN to get the associated card details.

    Args:
        card_bin: The card BIN to resolve.
    """
    return paystack_client.resolve_card_bin(card_bin)