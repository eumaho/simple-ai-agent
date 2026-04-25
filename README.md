
# LangChain VS Code Agent for WSL

A simple Python + LangChain agent project organized for this setup:

```text
Windows machine
└── WSL stores the project files
    └── VS Code opens the WSL folder
        └── Python virtual environment runs inside Linux
```

## What this app does

This is a small local AI agent that can:

- Chat with you from the VS Code terminal
- Decide when to use tools
- Call Python functions
- Return a final answer

Included tools:

- Cloud cost calculator
- Deployment risk checker
- Incident severity summarizer

## Project structure

```text
langchain-vscode-agent-wsl/
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   └── settings.json
├── docs/
│   └── ARCHITECTURE.md
├── scripts/
│   ├── setup_wsl.sh
│   └── run.sh
├── src/
│   └── agent_app/
│       ├── __init__.py
│       ├── agent.py
│       ├── config.py
│       ├── main.py
│       └── tools.py
├── tests/
│   └── test_tools.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Prerequisites on Windows

Install these first:

1. WSL with Ubuntu
2. VS Code
3. VS Code extension: **WSL**
4. Python 3.11+ inside WSL

Check Python from WSL:

```bash
python3 --version
```

## Recommended folder location

Store the project inside the WSL Linux filesystem, not under `/mnt/c`.

Good:

```bash
~/projects/langchain-vscode-agent-wsl
```

Avoid for this project:

```bash
/mnt/c/Users/yourname/projects/langchain-vscode-agent-wsl
```

The Linux filesystem is usually faster and cleaner for Python virtual environments.

## Setup steps

### 1. Unzip the project in WSL

From Windows, copy the zip somewhere accessible, then in WSL:

```bash
mkdir -p ~/projects
cd ~/projects
unzip /mnt/c/Users/YOUR_WINDOWS_USER/Downloads/langchain-vscode-agent-wsl.zip
cd langchain-vscode-agent-wsl
```

Adjust the path to wherever you downloaded the zip.

### 2. Open the folder in VS Code from WSL

From inside the project folder:

```bash
code .
```

VS Code should open in **WSL remote mode**.

You should see something like `WSL: Ubuntu` in the lower-left corner of VS Code.

### 3. Create the virtual environment and install dependencies

```bash
bash scripts/setup_wsl.sh
```

This creates:

```text
.venv/
```

and installs the packages from `requirements.txt`.

### 4. Configure your OpenAI API key

```bash
cp .env.example .env
nano .env
```

Set:

```bash
OPENAI_API_KEY=your_real_key_here
OPENAI_MODEL=gpt-4.1-mini
```

Save the file.

### 5. Run the app

```bash
source .venv/bin/activate
python -m agent_app.main
```

Or:

```bash
bash scripts/run.sh
```

You should see:

```text
Simple LangChain Agent
Type 'exit' or 'quit' to stop.
```

Try:

```text
If my server costs $0.42 per hour and runs all month, what is the monthly cost?
```

Try:

```text
What is the risk of deploying a database schema change on Friday afternoon?
```

Try:

```text
Users could not make payments for 25 minutes. What severity could this be?
```

## Run tests

```bash
source .venv/bin/activate
pytest
```

## Run from VS Code debugger

Open VS Code in WSL mode, then:

1. Go to **Run and Debug**
2. Select **Run LangChain Agent**
3. Press **F5**

The app will start in the integrated terminal.

## Where to add more tools

Add new tools in:

```text
src/agent_app/tools.py
```

Then register them in:

```text
src/agent_app/agent.py
```

Example:

```python
@tool
def get_customer_status(customer_id: str) -> str:
    """Look up customer status."""
    return "active"
```

Then add it to the `tools=[...]` list in `build_agent`.

## When LangChain is enough

LangChain is enough for:

- Learning
- Demos
- Tool-calling prototypes
- Small local automations
- Proofs of concept

## When to add LangGraph

Add LangGraph when you need:

- Multi-step workflows
- Human approval
- Durable execution
- Checkpoints
- Retry paths
- Branching logic
- More predictable control flow

## Suggested next evolution

After this version works, the next production-style steps are:

1. Add FastAPI
2. Add request/response logging
3. Add Redis or Postgres state
4. Add LangGraph workflow control
5. Add human approval before risky tools
6. Add tracing with LangSmith or Langfuse
7. Add a retrieval layer with a vector database
