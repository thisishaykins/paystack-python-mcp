from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from app.tools import *

# Initialize FastMCP server
mcp = FastMCP("paystack")

# Constants
PAYSTACK_API_BASE = "https://api.paystack.co"
USER_AGENT = "paystack-app/1.0"


async def paystack_get_request(endpoint: str, headers: dict[str, str]) -> dict[str, Any] | None:
    """Make a request to the Paystack API with proper error handling."""
    url = f"{PAYSTACK_API_BASE}/{endpoint}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

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
        

async def paystack_put_request(endpoint: str, headers: dict[str, str], data: dict[str, Any]) -> dict[str, Any] | None:
    """Make a PUT request to the Paystack API with proper error handling."""
    url = f"{PAYSTACK_API_BASE}/{endpoint}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(url, headers=headers, json=data, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        

async def paystack_delete_request(endpoint: str, headers: dict[str, str]) -> dict[str, Any] | None:
    """Make a DELETE request to the Paystack API with proper error handling."""
    url = f"{PAYSTACK_API_BASE}/{endpoint}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')