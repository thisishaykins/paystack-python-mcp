import pytest
from unittest.mock import patch, MagicMock


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
    with patch("app.tools.paystack_client", MagicMock()) as mock_client:
        yield mock_client


def test_get_balance(mock_paystack_client):
    from app.tools import get_balance

    get_balance()
    mock_paystack_client.get_balance.assert_called_once()


def test_get_balance_ledger(mock_paystack_client):
    from app.tools import get_balance_ledger

    get_balance_ledger()
    mock_paystack_client.get_balance_ledger.assert_called_once()


def test_list_customers(mock_paystack_client):
    from app.tools import list_customers

    list_customers()
    mock_paystack_client.list_customers.assert_called_once()


def test_create_customer(mock_paystack_client):
    from app.tools import create_customer

    create_customer("test@example.com", "John", "Doe")
    mock_paystack_client.create_customer.assert_called_once()


def test_fetch_customer(mock_paystack_client):
    from app.tools import fetch_customer

    fetch_customer("CUS_123")
    mock_paystack_client.fetch_customer.assert_called_once()


def test_update_customer(mock_paystack_client):
    from app.tools import update_customer

    update_customer("CUS_123", "John", "Doe")
    mock_paystack_client.update_customer.assert_called_once()


def test_list_products(mock_paystack_client):
    from app.tools import list_products

    list_products()
    mock_paystack_client.list_products.assert_called_once()


def test_create_product(mock_paystack_client):
    from app.tools import create_product

    create_product("Test Product", "A product for testing", 1000, "NGN")
    mock_paystack_client.create_product.assert_called_once()


def test_fetch_product(mock_paystack_client):
    from app.tools import fetch_product

    fetch_product("PROD_123")
    mock_paystack_client.fetch_product.assert_called_once()


def test_update_product(mock_paystack_client):
    from app.tools import update_product

    update_product("PROD_123", name="New Name")
    mock_paystack_client.update_product.assert_called_once()


def test_delete_product(mock_paystack_client):
    from app.tools import delete_product

    delete_product("PROD_123")
    mock_paystack_client.delete_product.assert_called_once()


def test_list_invoices(mock_paystack_client):
    from app.tools import list_invoices

    list_invoices()
    mock_paystack_client.list_invoices.assert_called_once()


def test_create_invoice(mock_paystack_client):
    from app.tools import create_invoice

    create_invoice("CUS_123", 5000)
    mock_paystack_client.create_invoice.assert_called_once()


def test_list_transactions(mock_paystack_client):
    from app.tools import list_transactions

    list_transactions()
    mock_paystack_client.list_transactions.assert_called_once()


def test_initialize_transaction(mock_paystack_client):
    from app.tools import initialize_transaction

    initialize_transaction("test@example.com", 2500, "NGN")
    mock_paystack_client.initialize_transaction.assert_called_once()


def test_verify_transaction(mock_paystack_client):
    from app.tools import verify_transaction

    verify_transaction("REF_123")
    mock_paystack_client.verify_transaction.assert_called_once()


def test_fetch_transaction(mock_paystack_client):
    from app.tools import fetch_transaction

    fetch_transaction("TRANS_123")
    mock_paystack_client.fetch_transaction.assert_called_once()


def test_get_transaction_timeline(mock_paystack_client):
    from app.tools import get_transaction_timeline

    get_transaction_timeline("TRANS_123")
    mock_paystack_client.get_transaction_timeline.assert_called_once()


def test_download_transactions(mock_paystack_client):
    from app.tools import download_transactions

    download_transactions()
    mock_paystack_client.download_transactions.assert_called_once()


def test_create_refund(mock_paystack_client):
    from app.tools import create_refund

    create_refund("TRANS_123")
    mock_paystack_client.create_refund.assert_called_once()


def test_list_subscriptions(mock_paystack_client):
    from app.tools import list_subscriptions

    list_subscriptions()
    mock_paystack_client.list_subscriptions.assert_called_once()


def test_disable_subscription(mock_paystack_client):
    from app.tools import disable_subscription

    disable_subscription("SUB_123", "TOKEN_123")
    mock_paystack_client.disable_subscription.assert_called_once()


def test_list_disputes(mock_paystack_client):
    from app.tools import list_disputes

    list_disputes()
    mock_paystack_client.list_disputes.assert_called_once()


def test_fetch_dispute(mock_paystack_client):
    from app.tools import fetch_dispute

    fetch_dispute("DIS_123")
    mock_paystack_client.fetch_dispute.assert_called_once()


def test_download_dispute(mock_paystack_client):
    from app.tools import download_dispute

    download_dispute()
    mock_paystack_client.download_dispute.assert_called_once()


def test_resolve_dispute(mock_paystack_client):
    from app.tools import resolve_dispute

    resolve_dispute("DIS_123", "resolved", "Message", "1000", "file.pdf")
    mock_paystack_client.resolve_dispute.assert_called_once()


def test_add_evidence_to_dispute(mock_paystack_client):
    from app.tools import add_evidence_to_dispute

    add_evidence_to_dispute(
        "DIS_123", "test@example.com", "John Doe", "12345", "Details"
    )
    mock_paystack_client.add_evidence_to_dispute.assert_called_once()


def test_create_payment_page(mock_paystack_client):
    from app.tools import create_payment_page

    create_payment_page("Test Page", 1000)
    mock_paystack_client.create_payment_page.assert_called_once()


def test_list_payment_pages(mock_paystack_client):
    from app.tools import list_payment_pages

    list_payment_pages()
    mock_paystack_client.list_payment_pages.assert_called_once()


def test_fetch_payment_page(mock_paystack_client):
    from app.tools import fetch_payment_page

    fetch_payment_page("PAGE_123")
    mock_paystack_client.fetch_payment_page.assert_called_once()


def test_update_payment_page(mock_paystack_client):
    from app.tools import update_payment_page

    update_payment_page("PAGE_123", name="New Page Name")
    mock_paystack_client.update_payment_page.assert_called_once()


def test_disable_payment_page(mock_paystack_client):
    from app.tools import disable_payment_page

    disable_payment_page("PAGE_123")
    mock_paystack_client.disable_payment_page.assert_called_once()


def test_enable_payment_page(mock_paystack_client):
    from app.tools import enable_payment_page

    enable_payment_page("PAGE_123")
    mock_paystack_client.enable_payment_page.assert_called_once()


def test_add_products_to_payment_page(mock_paystack_client):
    from app.tools import add_products_to_payment_page

    add_products_to_payment_page("PAGE_123", ["PROD_123"])
    mock_paystack_client.add_products_to_payment_page.assert_called_once()


def test_create_plan(mock_paystack_client):
    from app.tools import create_plan

    create_plan("Test Plan", 1000, "monthly")
    mock_paystack_client.create_plan.assert_called_once()


def test_list_plans(mock_paystack_client):
    from app.tools import list_plans

    list_plans()
    mock_paystack_client.list_plans.assert_called_once()


def test_fetch_plan(mock_paystack_client):
    from app.tools import fetch_plan

    fetch_plan("PLAN_123")
    mock_paystack_client.fetch_plan.assert_called_once()


def test_fetch_banks(mock_paystack_client):
    from app.tools import fetch_banks

    fetch_banks(country="NG")
    mock_paystack_client.fetch_banks.assert_called_once()


def test_list_avs(mock_paystack_client):
    from app.tools import list_avs

    list_avs(country="Nigeria")
    mock_paystack_client.list_avs.assert_called_once()


def test_list_countries(mock_paystack_client):
    from app.tools import list_countries

    list_countries()
    mock_paystack_client.list_countries.assert_called_once()


def test_resolve_account_number(mock_paystack_client):
    from app.tools import resolve_account_number

    resolve_account_number("1234567890", "058")
    mock_paystack_client.resolve_account_number.assert_called_once()


def test_resolve_card_bin(mock_paystack_client):
    from app.tools import resolve_card_bin

    resolve_card_bin("539983")
    mock_paystack_client.resolve_card_bin.assert_called_once()
