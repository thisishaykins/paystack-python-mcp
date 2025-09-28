# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install uv, the project's package manager
RUN pip install uv

# Copy the dependency definition files
COPY pyproject.toml uv.lock ./

# Install project dependencies into the system's Python environment
# Using --system is recommended for containers as there's no need for a venv
RUN uv pip install --system --no-cache .

# Copy the rest of the application source code into the container
COPY . .

# Set the command to run when the container launches
CMD ["python", "mcp_server.py"]