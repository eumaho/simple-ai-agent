
# AI Agent System Architecture

This project is intentionally small, but it follows the same layered shape used by production AI agent systems.

## Layers

### 1. User & Channel Layer

This is where requests enter the system.

Examples:

- VS Code terminal
- CLI
- Web app
- Slack or Teams
- REST API

In this sample project, the channel is the VS Code integrated terminal.

### 2. API / Application Layer

In a larger system, this would usually be FastAPI or another backend service.

Responsibilities:

- Authentication
- Authorization
- Request validation
- Rate limits
- Session handling

This sample project does not expose an API yet. The app runs locally from the command line.

### 3. Agent Orchestration Layer

This is the core of the system.

In this project, LangChain is responsible for:

- Connecting the LLM to tools
- Letting the model decide when to call a tool
- Returning the final answer to the user

For more complex production workflows, LangGraph can be added for:

- Durable execution
- Human-in-the-loop approvals
- State machines
- Multi-step workflow control
- Checkpointing

### 4. LLM Layer

The LLM performs reasoning and decides whether a tool is needed.

This project uses:

- `ChatOpenAI`
- OpenAI model configured by `OPENAI_MODEL`

### 5. Tool & Action Layer

Tools are Python functions exposed to the agent.

This project includes:

- `calculate_monthly_cloud_cost`
- `check_deployment_risk`
- `summarize_incident_severity`

This is the most important mental model:

```text
LLM + tools + control flow = agent
```

### 6. Retrieval & Knowledge Layer

This project does not include retrieval yet.

In a real system, this layer may include:

- Embeddings
- Vector database
- Document store
- Knowledge base
- File search
- SQL database

### 7. Memory & State Layer

This project is stateless for simplicity.

In a real system, you may use:

- Redis for short-term state
- Postgres for durable state
- LangGraph checkpointing
- Conversation history storage

### 8. Infrastructure & Operations Layer

For local development, this project uses:

- WSL
- VS Code
- Python virtual environment

For production, this layer may include:

- Docker
- CI/CD
- Secrets manager
- Logging
- Monitoring
- Queues and background jobs

## Cross-cutting concerns

### Security & Guardrails

Add these before production use:

- Input validation
- Tool allowlists
- Human approval for risky actions
- Secrets management
- PII protection
- Output filtering
- Audit logging

### Observability & Evaluation

Add these before production use:

- Logs
- Traces
- Tool-call visibility
- Prompt debugging
- Evaluation test sets
- Regression tests
- Quality metrics
