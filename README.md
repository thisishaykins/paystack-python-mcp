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

| Tool | Description |
| --- | --- |
| `balance.read` | Retrieves the balance from a Paystack account. |
| `coupon.create` | Creates a new coupon. |
| `coupon.list` | Retrieves a list of all coupons. |
| `customer.create` | Creates a new customer. |
| `customer.list` | Retrieves a list of all customers. |
| `customer.read` | Fetches the details of a specific customer. |
| `customer.update` | Updates the details of a specific customer. |
| `dispute.add_evidence` | Adds evidence to a dispute. |
| `dispute.list` | Retrieves a list of all disputes. |
| `invoice.create` | Creates a new invoice. |
| `invoice.list` | Retrieves a list of all invoices. |
| `payment_page.create` | Creates a new payment page. |
| `plan.create` | Creates a new subscription plan. |
| `plan.list` | Retrieves a list of all subscription plans. |
| `plan.read` | Fetches the details of a specific subscription plan. |
| `price.create` | Creates a new price. |
| `price.list` | Retrieves a list of all prices. |
| `product.create` | Creates a new product. |
| `product.list` | Retrieves a list of all products. |
| `refund.create` | Creates a new refund. |
| `subscription.disable` | Disables a subscription. |
| `subscription.list` | Retrieves a list of all subscriptions. |
| `transaction.initialize` | Initializes a new transaction. |
| `transaction.list` | Retrieves a list of all transactions. |
| `transaction.read` | Fetches the details of a specific transaction. |
| `transaction.verify` | Verifies the status of a transaction. |
| `verification.resolve_account_number` | Resolves an account number to get the account holder's name. |

## Usage with an AI Assistant (e.g., Claude)

You can connect this MCP server to an AI assistant like Claude to allow it to perform actions on your behalf. The assistant can call the tools by sending a JSON-RPC request to the server.

Here is an example of how Claude could use the `customer.create` tool:

**User:** "Please create a new customer with the email address 'test@example.com' and the name 'Test User'."

**Claude's Thought Process:** "The user wants to create a new customer. I will use the `customer.create` tool. I need to extract the email, first name, and last name from the user's request."

**Claude's Tool Call:**
```json
{
  "tool_name": "customer.create",
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