"""Weather Agent MCP

A simple agent that fetches weather for a city using Claude + tools.

Usage:
    python research_agent.py
"""

from __future__ import annotations

import json
import os
from pathlib import Path

_env_path = Path(__file__).resolve().parents[2] / ".env"
if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

import anthropic

TOOLS = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"},
            },
            "required": ["city"],
        },
    },
]


def get_weather(city: str) -> str:
    """Simulated weather lookup."""
    data = {
        "new york": {"temp": 42, "condition": "Cloudy", "humidity": 65},
        "san francisco": {"temp": 58, "condition": "Foggy", "humidity": 78},
        "london": {"temp": 38, "condition": "Rainy", "humidity": 85},
    }
    result = data.get(city.lower(), {"temp": 55, "condition": "Clear", "humidity": 50})
    return json.dumps({"city": city, **result})


def run_agent(question: str) -> str:
    client = anthropic.Anthropic()
    messages: list[dict] = [{"role": "user", "content": question}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
        )

        tool_calls = [b for b in response.content if b.type == "tool_use"]

        if not tool_calls:
            final_text = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_text += block.text
            return final_text

        tool_results = []
        for tool_call in tool_calls:
            result = get_weather(tool_call.input["city"])
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tool_call.id,
                "content": result,
            })

        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})


def main() -> None:
    answer = run_agent("What's the weather in New York?")
    print(answer)


if __name__ == "__main__":
    main()
