# Launch Guide: Weather Agent MCP

A simple MCP that fetches weather for a city using Claude.

## Prerequisites

- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com/)

## Setup

```bash
git clone <repo-url>
cd TestMCP
python -m venv venv
source venv/bin/activate   # macOS/Linux
pip install anthropic
```

## Configure API Key

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

Or create a `.env` file two directories above the script:

```
ANTHROPIC_API_KEY=sk-ant-...
```

## Run

```bash
python research_agent.py
```

This will fetch the weather for New York and print the result. Edit the question in `main()` to query any city.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: anthropic` | Run `pip install anthropic` |
| `AuthenticationError` | Check that `ANTHROPIC_API_KEY` is set |
