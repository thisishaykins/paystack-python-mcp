from app.server import mcp
# The tools are decorated with the mcp instance, so they need to be imported
# after the mcp object is created.
from app.tools import *

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')