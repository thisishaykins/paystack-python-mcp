# Paystack MCP Server

This project is a Machine-Centric Programming (MCP) server for the Paystack API. It provides a set of tools that can be used by AI assistants and other automated systems to interact with Paystack in a structured way. This allows for the automation of tasks suchs as creating customers, managing products, and initiating transactions.

This server is built using the official `paystack-sdk` for Python and `FastMCP` for the server implementation.

## Features

- A comprehensive set of tools for interacting with the Paystack API.
- Asynchronous by default, built on `FastMCP`.
- Easy to extend with new tools and functionality.
- Includes a `Dockerfile` for easy containerization and deployment.

## Installation

This project uses `uv` for dependency management. To install the necessary packages, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd paystack-python-mcp
    ```

2.  **Create a virtual environment:**
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Install the dependencies:**
    ```bash
    uv pip install -e .
    ```

## Setup

To use the Paystack MCP server, you need to provide your Paystack API key. The server is configured to read the API key from an environment variable.

1.  **Create a `.env` file** in the root of the project.
2.  **Add your API key** to the `.env` file:
    ```
    PAYSTACK_API_KEY=sk_your_secret_key
    ```

## Running the Server

To run the MCP server, execute the following command from the root of the project:

```bash
python mcp_server.py
```

The server will start and listen for requests on `stdio`.

## Available Tools

The following tools are available through the MCP server:

### Balance
- `get_balance()`: Retrieves the balance from a Paystack account.

### Customers
- `list_customers()`: Retrieves a list of all customers.
- `create_customer(email: str, first_name: str, last_name: str)`: Creates a new customer.

### Products
- `list_products()`: Retrieves a list of all products.
- `create_product(name: str, description: str, price: int, currency: str)`: Creates a new product.

### Prices
- `list_prices()`: Retrieves a list of all prices.
- `create_price(currency: str, amount: int, name: str)`: Creates a new price.

### Invoices
- `list_invoices()`: Retrieves a list of all invoices.
- `create_invoice(customer: str, amount: int)`: Creates a new invoice.

### Transactions
- `list_transactions()`: Retrieves a list of all transactions.

### Refunds
- `create_refund(transaction: str, amount: int | None = None)`: Creates a new refund.

### Subscriptions
- `list_subscriptions()`: Retrieves a list of all subscriptions.
- `disable_subscription(code: str, token: str)`: Disables a subscription.

### Coupons
- `list_coupons()`: Retrieves a list of all coupons.
- `create_coupon(coupon: str, amount_off: int)`: Creates a new coupon.

### Disputes
- `list_disputes()`: Retrieves a list of all disputes.
- `add_evidence_to_dispute(dispute_id: str, customer_email: str, customer_name: str, customer_phone: str, service_details: str)`: Adds evidence to a dispute.

### Payment Pages
- `create_payment_page(name: str, amount: int)`: Creates a new payment page.

## Usage with an AI Assistant (e.g., Claude)

You can connect this MCP server to an AI assistant like Claude to allow it to perform actions on your behalf. The assistant can call the tools by sending a JSON-RPC request to the server.

Here is an example of how Claude could use the `create_customer` tool:

**User:** "Please create a new customer with the email address 'test@example.com' and the name 'Test User'."

**Claude's Thought Process:** "The user wants to create a new customer. I will use the `create_customer` tool. I need to extract the email, first name, and last name from the user's request."

**Claude's Tool Call:**
```json
{
  "tool_name": "create_customer",
  "parameters": {
    "email": "test@example.com",
    "first_name": "Test",
    "last_name": "User"
  }
}
```

The MCP server would then execute the tool and return the result to Claude.

## Build using Docker

This project includes a `Dockerfile` to make it easy to build and run the server in a container.

1.  **Build the Docker image:**
    ```bash
    docker build -t paystack-mcp-server .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -it --rm -e PAYSTACK_API_KEY=sk_your_secret_key paystack-mcp-server
    ```

This will start the server inside a Docker container.