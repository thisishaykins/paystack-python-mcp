from app.server import mcp
from app.paystack_client import paystack_client


@mcp.tool(name="balance.read")
async def get_balance():
    """
    Retrieves the balance from a Paystack account.
    """
    return await paystack_client.get_balance()


@mcp.tool(name="balance.ledger")
async def get_balance_ledger():
    """
    Retrieves the balance ledger from a Paystack account.
    """
    return await paystack_client.get_balance_ledger()


@mcp.tool(name="customer.list")
async def list_customers():
    """
    Retrieves a list of all customers.
    """
    return await paystack_client.list_customers()


@mcp.tool(name="customer.create")
async def create_customer(
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
    return await paystack_client.create_customer(email, first_name, last_name, phone)


@mcp.tool(name="customer.read")
async def fetch_customer(customer_code: str):
    """
    Fetches the details of a specific customer.

    Args:
        customer_code: The code of the customer to fetch.
    """
    return await paystack_client.fetch_customer(customer_code)


@mcp.tool(name="customer.update")
async def update_customer(
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
    return await paystack_client.update_customer(code, first_name, last_name, phone)


@mcp.tool(name="product.list")
async def list_products():
    """
    Retrieves a list of all products.
    """
    return await paystack_client.list_products()


@mcp.tool(name="product.create")
async def create_product(
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
    return await paystack_client.create_product(
        name, description, price, currency, quantity
    )


@mcp.tool(name="product.read")
async def fetch_product(product_code: str):
    """
    Fetches the details of a specific product.

    Args:
        product_code: The code of the product to fetch.
    """
    return await paystack_client.fetch_product(product_code)


@mcp.tool(name="product.update")
async def update_product(
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
    return await paystack_client.update_product(
        product_code, name, description, price, currency, quantity
    )


@mcp.tool(name="product.delete")
async def delete_product(product_code: str):
    """
    Deletes a specific product.
    Args:
        product_code: The code of the product to delete.
    """
    return await paystack_client.delete_product(product_code)


@mcp.tool(name="invoice.list")
async def list_invoices():
    """
    Retrieves a list of all invoices.
    """
    return await paystack_client.list_invoices()


@mcp.tool(name="invoice.create")
async def create_invoice(customer: str, amount: int):
    """
    Creates a new invoice.

    Args:
        customer: The customer's code or email address.
        amount: The amount of the invoice in the smallest currency unit (e.g., kobo).
    """
    return await paystack_client.create_invoice(customer, amount)


@mcp.tool(name="transaction.list")
async def list_transactions():
    """
    Retrieves a list of all transactions.
    """
    return await paystack_client.list_transactions()


@mcp.tool(name="transaction.initialize")
async def initialize_transaction(email: str, amount: int, currency: str):
    """
    Initializes a new transaction.

    Args:
        email: The customer's email address.
        amount: The amount of the transaction in the smallest currency unit (e.g., kobo).
        currency: The currency of the transaction (e.g., NGN).
    """
    return await paystack_client.initialize_transaction(email, amount, currency)


@mcp.tool(name="transaction.verify")
async def verify_transaction(reference: str):
    """
    Verifies the status of a transaction.

    Args:
        reference: The reference of the transaction to verify.
    """
    return await paystack_client.verify_transaction(reference)


@mcp.tool(name="transaction.read")
async def fetch_transaction(transaction_id: str):
    """
    Fetches the details of a specific transaction.

    Args:
        transaction_id: The ID of the transaction to fetch.
    """
    return await paystack_client.fetch_transaction(transaction_id)


@mcp.tool(name="transaction.timeline")
async def get_transaction_timeline(transaction_id_or_reference: str):
    """
    Retrieves the timeline of a specific transaction.

    Args:
        transaction_id_or_reference: The ID/Reference of the transaction to get the timeline for.
    """
    return await paystack_client.get_transaction_timeline(transaction_id_or_reference)


@mcp.tool(name="transaction.download")
async def download_transactions(
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
    return await paystack_client.download_transactions(
        per_page, page, from_date, to_date
    )


@mcp.tool(name="refund.create")
async def create_refund(transaction: str, amount: int | None = None):
    """
    Creates a new refund.

    Args:
        transaction: The transaction reference or ID to refund.
        amount: The amount to refund in the smallest currency unit (e.g., kobo).
                If not provided, a full refund will be issued.
    """
    return await paystack_client.create_refund(transaction, amount)


@mcp.tool(name="subscription.list")
async def list_subscriptions():
    """
    Retrieves a list of all subscriptions.
    """
    return await paystack_client.list_subscriptions()


@mcp.tool(name="subscription.disable")
async def disable_subscription(code: str, token: str):
    """
    Disables a subscription.

    Args:
        code: The subscription code.
        token: The email token of the customer.
    """
    return await paystack_client.disable_subscription(code, token)


@mcp.tool(name="dispute.list")
async def list_disputes():
    """
    Retrieves a list of all disputes.
    """
    return await paystack_client.list_disputes()


@mcp.tool(name="dispute.read")
async def fetch_dispute(dispute_id: str):
    """
    Fetches the details of a specific dispute.

    Args:
        dispute_id: The ID of the dispute to fetch.
    """
    return await paystack_client.fetch_dispute(dispute_id)


@mcp.tool(name="dispute.download")
async def download_dispute(
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
    return await paystack_client.download_dispute(per_page, page, from_date, to_date)


@mcp.tool(name="dispute.resolve")
async def resolve_dispute(
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
    return await paystack_client.resolve_dispute(
        dispute_id, resolution, message, refund_amount, uploaded_filename, evidence
    )


@mcp.tool(name="dispute.add_evidence")
async def add_evidence_to_dispute(
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
    return await paystack_client.add_evidence_to_dispute(
        dispute_id, customer_email, customer_name, customer_phone, service_details
    )


@mcp.tool(name="payment_page.create")
async def create_payment_page(name: str, amount: int, description: str | None = None):
    """
    Creates a new payment page.

    Args:
        name: The name of the payment page.
        amount: The amount for the payment page in the smallest currency unit (e.g., kobo).
        description: A description for the payment page (optional).
    """
    return await paystack_client.create_payment_page(name, amount, description)


@mcp.tool(name="payment_page.list")
async def list_payment_pages():
    """
    Retrieves a list of all payment pages.
    """
    return await paystack_client.list_payment_pages()


@mcp.tool(name="payment_page.read")
async def fetch_payment_page(id: str):
    """
    Fetches the details of a specific payment page.

    Args:
        id: The id of the payment page to fetch.
    """
    return await paystack_client.fetch_payment_page(id)


@mcp.tool(name="payment_page.update")
async def update_payment_page(
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
    return await paystack_client.update_payment_page(id, name, description, amount)


@mcp.tool(name="payment_page.disable")
async def disable_payment_page(id: str):
    """
    Disables a specific payment page.
    Args:
        id: The id of the payment page to disable.
    """
    return await paystack_client.disable_payment_page(id)


@mcp.tool(name="payment_page.enable")
async def enable_payment_page(id: str):
    """
    Enables a specific payment page.
    Args:
        id: The id of the payment page to enable.
    """
    return await paystack_client.enable_payment_page(id)


@mcp.tool(name="payment_page.add_products")
async def add_products_to_payment_page(id: str, products: list[str]):
    """
    Adds products to a specific payment page.
    Args:
        id: The id of the payment page to add products to.
        products: A list of product codes to add to the payment page.
    """
    return await paystack_client.add_products_to_payment_page(id, products)


@mcp.tool(name="plan.create")
async def create_plan(name: str, amount: int, interval: str):
    """
    Creates a new subscription plan.

    Args:
        name: The name of the plan.
        amount: The amount for the plan in the smallest currency unit (e.g., kobo).
        interval: The frequency of the plan (e.g., 'daily', 'weekly', 'monthly').
    """
    return await paystack_client.create_plan(name, amount, interval)


@mcp.tool(name="plan.list")
async def list_plans():
    """
    Retrieves a list of all subscription plans.
    """
    return await paystack_client.list_plans()


@mcp.tool(name="plan.read")
async def fetch_plan(plan_code: str):
    """
    Fetches the details of a specific subscription plan.

    Args:
        plan_code: The code of the plan to fetch.
    """
    return await paystack_client.fetch_plan(plan_code)


@mcp.tool(name="verification.fetch_banks")
async def fetch_banks(
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
    return await paystack_client.fetch_banks(
        country, pay_with_bank_transfer, use_cursor, per_page, next, previous, gateway
    )


@mcp.tool(name="verification.list_avs")
async def list_avs(country: str, type: str | None = None, currency: str | None = None):
    """
    Lists all available account verification services.
    Args:
        country: The country code to filter by.
        type: The type of verification service to filter by (optional).
        currency: The currency code to filter by (optional).
    """
    return await paystack_client.list_avs(country, type, currency)


@mcp.tool(name="verification.list_countries")
async def list_countries():
    """
    Retrieves a list of all countries.
    """
    return await paystack_client.list_countries()


@mcp.tool(name="verification.resolve_account_number")
async def resolve_account_number(account_number: str, bank_code: str):
    """
    Resolves an account number to get the account holder's name.

    Args:
        account_number: The account number to resolve.
        bank_code: The bank code of the account's bank.
    """
    return await paystack_client.resolve_account_number(account_number, bank_code)


@mcp.tool(name="verification.resolve_card_bin")
async def resolve_card_bin(card_bin: str):
    """
    Resolves a card BIN to get the associated card details.

    Args:
        card_bin: The card BIN to resolve.
    """
    return await paystack_client.resolve_card_bin(card_bin)