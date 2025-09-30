import pytest
from unittest.mock import patch, AsyncMock

# Import app.server before app.tools to avoid circular dependency
from app import server
from app import tools

pytestmark = pytest.mark.asyncio


@pytest.fixture(autouse=True)
def mock_env_vars():
    """
    Mock environment variables to avoid errors during test collection.
    """
    with patch.dict("os.environ", {"PAYSTACK_API_KEY": "test_key"}):
        yield


@pytest.fixture
def mock_paystack_client():
    """
    Mock the paystack_client to avoid actual API calls during tests.
    """
    with patch.object(
        tools.paystack_client, "_instance", new_callable=AsyncMock
    ) as mock_client:
        yield mock_client


async def test_get_balance(mock_paystack_client):
    await tools.get_balance()
    mock_paystack_client.get_balance.assert_awaited_once()


async def test_get_balance_ledger(mock_paystack_client):
    await tools.get_balance_ledger()
    mock_paystack_client.get_balance_ledger.assert_awaited_once()


async def test_list_customers(mock_paystack_client):
    await tools.list_customers()
    mock_paystack_client.list_customers.assert_awaited_once()


async def test_create_customer(mock_paystack_client):
    await tools.create_customer("test@example.com", "John", "Doe")
    mock_paystack_client.create_customer.assert_awaited_once_with(
        "test@example.com", "John", "Doe", None
    )


async def test_fetch_customer(mock_paystack_client):
    await tools.fetch_customer("CUS_123")
    mock_paystack_client.fetch_customer.assert_awaited_once_with("CUS_123")


async def test_update_customer(mock_paystack_client):
    await tools.update_customer("CUS_123", "John", "Doe")
    mock_paystack_client.update_customer.assert_awaited_once_with(
        "CUS_123", "John", "Doe", None
    )


async def test_list_products(mock_paystack_client):
    await tools.list_products()
    mock_paystack_client.list_products.assert_awaited_once()


async def test_create_product(mock_paystack_client):
    await tools.create_product("Test Product", "A product for testing", 1000, "NGN")
    mock_paystack_client.create_product.assert_awaited_once_with(
        "Test Product", "A product for testing", 1000, "NGN", 1
    )


async def test_fetch_product(mock_paystack_client):
    await tools.fetch_product("PROD_123")
    mock_paystack_client.fetch_product.assert_awaited_once_with("PROD_123")


async def test_update_product(mock_paystack_client):
    await tools.update_product("PROD_123", name="New Name")
    mock_paystack_client.update_product.assert_awaited_once_with(
        "PROD_123", "New Name", None, None, None, None
    )


async def test_delete_product(mock_paystack_client):
    await tools.delete_product("PROD_123")
    mock_paystack_client.delete_product.assert_awaited_once_with("PROD_123")


async def test_list_invoices(mock_paystack_client):
    await tools.list_invoices()
    mock_paystack_client.list_invoices.assert_awaited_once()


async def test_create_invoice(mock_paystack_client):
    await tools.create_invoice("CUS_123", 5000)
    mock_paystack_client.create_invoice.assert_awaited_once_with("CUS_123", 5000)


async def test_list_transactions(mock_paystack_client):
    await tools.list_transactions()
    mock_paystack_client.list_transactions.assert_awaited_once()


async def test_initialize_transaction(mock_paystack_client):
    await tools.initialize_transaction("test@example.com", 2500, "NGN")
    mock_paystack_client.initialize_transaction.assert_awaited_once_with(
        "test@example.com", 2500, "NGN"
    )


async def test_verify_transaction(mock_paystack_client):
    await tools.verify_transaction("REF_123")
    mock_paystack_client.verify_transaction.assert_awaited_once_with("REF_123")


async def test_fetch_transaction(mock_paystack_client):
    await tools.fetch_transaction("TRANS_123")
    mock_paystack_client.fetch_transaction.assert_awaited_once_with("TRANS_123")


async def test_get_transaction_timeline(mock_paystack_client):
    await tools.get_transaction_timeline("TRANS_123")
    mock_paystack_client.get_transaction_timeline.assert_awaited_once_with("TRANS_123")


async def test_download_transactions(mock_paystack_client):
    await tools.download_transactions()
    mock_paystack_client.download_transactions.assert_awaited_once_with(
        50, 1, None, None
    )


async def test_create_refund(mock_paystack_client):
    await tools.create_refund("TRANS_123")
    mock_paystack_client.create_refund.assert_awaited_once_with("TRANS_123", None)


async def test_list_subscriptions(mock_paystack_client):
    await tools.list_subscriptions()
    mock_paystack_client.list_subscriptions.assert_awaited_once()


async def test_disable_subscription(mock_paystack_client):
    await tools.disable_subscription("SUB_123", "TOKEN_123")
    mock_paystack_client.disable_subscription.assert_awaited_once_with(
        "SUB_123", "TOKEN_123"
    )


async def test_list_disputes(mock_paystack_client):
    await tools.list_disputes()
    mock_paystack_client.list_disputes.assert_awaited_once()


async def test_fetch_dispute(mock_paystack_client):
    await tools.fetch_dispute("DIS_123")
    mock_paystack_client.fetch_dispute.assert_awaited_once_with("DIS_123")


async def test_download_dispute(mock_paystack_client):
    await tools.download_dispute()
    mock_paystack_client.download_dispute.assert_awaited_once_with(50, 1, None, None)


async def test_resolve_dispute(mock_paystack_client):
    await tools.resolve_dispute("DIS_123", "resolved", "Message", "1000", "file.pdf")
    mock_paystack_client.resolve_dispute.assert_awaited_once_with(
        "DIS_123", "resolved", "Message", "1000", "file.pdf", None
    )


async def test_add_evidence_to_dispute(mock_paystack_client):
    await tools.add_evidence_to_dispute(
        "DIS_123", "test@example.com", "John Doe", "12345", "Details"
    )
    mock_paystack_client.add_evidence_to_dispute.assert_awaited_once_with(
        "DIS_123", "test@example.com", "John Doe", "12345", "Details"
    )


async def test_create_payment_page(mock_paystack_client):
    await tools.create_payment_page("Test Page", 1000, "A test page")
    mock_paystack_client.create_payment_page.assert_awaited_once_with(
        "Test Page", 1000, "A test page"
    )


async def test_list_payment_pages(mock_paystack_client):
    await tools.list_payment_pages()
    mock_paystack_client.list_payment_pages.assert_awaited_once()


async def test_fetch_payment_page(mock_paystack_client):
    await tools.fetch_payment_page("PAGE_123")
    mock_paystack_client.fetch_payment_page.assert_awaited_once_with("PAGE_123")


async def test_update_payment_page(mock_paystack_client):
    await tools.update_payment_page("PAGE_123", name="New Page Name")
    mock_paystack_client.update_payment_page.assert_awaited_once_with(
        "PAGE_123", "New Page Name", None, None
    )


async def test_disable_payment_page(mock_paystack_client):
    await tools.disable_payment_page("PAGE_123")
    mock_paystack_client.disable_payment_page.assert_awaited_once_with("PAGE_123")


async def test_enable_payment_page(mock_paystack_client):
    await tools.enable_payment_page("PAGE_123")
    mock_paystack_client.enable_payment_page.assert_awaited_once_with("PAGE_123")


async def test_add_products_to_payment_page(mock_paystack_client):
    await tools.add_products_to_payment_page("PAGE_123", ["PROD_123"])
    mock_paystack_client.add_products_to_payment_page.assert_awaited_once_with(
        "PAGE_123", ["PROD_123"]
    )


async def test_create_plan(mock_paystack_client):
    await tools.create_plan("Test Plan", 1000, "monthly")
    mock_paystack_client.create_plan.assert_awaited_once_with(
        "Test Plan", 1000, "monthly"
    )


async def test_list_plans(mock_paystack_client):
    await tools.list_plans()
    mock_paystack_client.list_plans.assert_awaited_once()


async def test_fetch_plan(mock_paystack_client):
    await tools.fetch_plan("PLAN_123")
    mock_paystack_client.fetch_plan.assert_awaited_once_with("PLAN_123")


async def test_fetch_banks(mock_paystack_client):
    await tools.fetch_banks(country="NG")
    mock_paystack_client.fetch_banks.assert_awaited_once_with(
        "NG", None, None, None, None, None, None
    )


async def test_list_avs(mock_paystack_client):
    await tools.list_avs(country="Nigeria")
    mock_paystack_client.list_avs.assert_awaited_once_with("Nigeria", None, None)


async def test_list_countries(mock_paystack_client):
    await tools.list_countries()
    mock_paystack_client.list_countries.assert_awaited_once()


async def test_resolve_account_number(mock_paystack_client):
    await tools.resolve_account_number("1234567890", "058")
    mock_paystack_client.resolve_account_number.assert_awaited_once_with(
        "1234567890", "058"
    )


async def test_resolve_card_bin(mock_paystack_client):
    await tools.resolve_card_bin("539983")
    mock_paystack_client.resolve_card_bin.assert_awaited_once_with("539983")