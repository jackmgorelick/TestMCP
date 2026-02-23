"""Weather MCP Server

An MCP server that exposes a single tool to fetch weather for a city.

Usage:
    python research_agent.py
"""

import json

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather Agent")


@mcp.tool()
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    data = {
        "new york": {"temp": 42, "condition": "Cloudy", "humidity": 65},
        "san francisco": {"temp": 58, "condition": "Foggy", "humidity": 78},
        "london": {"temp": 38, "condition": "Rainy", "humidity": 85},
    }
    result = data.get(city.lower(), {"temp": 55, "condition": "Clear", "humidity": 50})
    return json.dumps({"city": city, **result})


if __name__ == "__main__":
    mcp.run(transport="stdio")
