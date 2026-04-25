
from agent_app.agent import ask_agent, build_agent
from agent_app.config import load_config


EXAMPLE_QUESTIONS = [
    "If my server costs $0.42 per hour and runs all month, what is the monthly cost?",
    "What is the risk of deploying a database schema change on Friday afternoon?",
    "Users could not make payments for 25 minutes. What severity could this be?",
]


def run_demo() -> None:
    config = load_config()
    agent = build_agent(config)

    for question in EXAMPLE_QUESTIONS:
        print("\n" + "=" * 100)
        print(f"USER: {question}")
        print("-" * 100)

        answer = ask_agent(agent, question)

        print(f"AGENT: {answer}")


def run_interactive() -> None:
    config = load_config()
    agent = build_agent(config)

    print("Simple LangChain Agent")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            return

        if not question:
            continue

        answer = ask_agent(agent, question)
        print(f"Agent: {answer}\n")


if __name__ == "__main__":
    # Change to run_demo() if you want fixed sample questions.
    run_interactive()
