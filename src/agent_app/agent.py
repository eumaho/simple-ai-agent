
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from agent_app.config import AppConfig
from agent_app.tools import (
    calculate_monthly_cloud_cost,
    check_deployment_risk,
    summarize_incident_severity,
)


SYSTEM_PROMPT = """
You are a practical software engineering assistant.

Rules:
- Use tools only when they improve the answer.
- Do not invent tool results.
- Keep answers concise, structured, and useful for software engineers.
- For risky production actions, recommend human approval and rollback planning.
- If the user asks for cost, deployment risk, or incident severity, consider using a tool.
"""


def build_agent(config: AppConfig):
    """Build the LangChain tool-calling agent."""
    model = ChatOpenAI(
        model=config.openai_model,
        temperature=0,
        api_key=config.openai_api_key,
    )

    return create_agent(
        model=model,
        tools=[
            calculate_monthly_cloud_cost,
            check_deployment_risk,
            summarize_incident_severity,
        ],
        system_prompt=SYSTEM_PROMPT,
    )


def ask_agent(agent, question: str) -> str:
    """Invoke the agent and return the final response text."""
    response = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": question},
            ]
        }
    )

    return response["messages"][-1].content
