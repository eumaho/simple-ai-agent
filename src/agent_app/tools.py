
from langchain.tools import tool


@tool
def calculate_monthly_cloud_cost(
    hourly_cost: float,
    hours_per_day: int = 24,
    days: int = 30,
) -> float:
    """
    Calculate estimated monthly cloud cost.

    Args:
        hourly_cost: Cost per hour in dollars.
        hours_per_day: Number of hours used per day.
        days: Number of days in the month.

    Returns:
        Estimated monthly cost in dollars.
    """
    return round(hourly_cost * hours_per_day * days, 2)


@tool
def check_deployment_risk(change_type: str) -> str:
    """
    Give a simple deployment risk assessment based on the type of software change.

    Args:
        change_type: Type of software change.

    Returns:
        Risk level and recommendation.
    """
    normalized = change_type.lower()

    if "database" in normalized or "schema" in normalized or "migration" in normalized:
        return (
            "High risk. Use migration scripts, backups, rollback plan, staging validation, "
            "and post-deployment monitoring."
        )

    if "auth" in normalized or "permission" in normalized or "security" in normalized:
        return (
            "High risk. Require peer review, security review, tests for authorization edge cases, "
            "and a rollback plan."
        )

    if "config" in normalized or "environment" in normalized:
        return (
            "Medium to high risk. Validate configuration, use version control, "
            "compare environments, and prepare rollback."
        )

    if "ui" in normalized or "frontend" in normalized:
        return (
            "Medium risk. Use feature flags, browser testing, analytics, and error monitoring."
        )

    return "Low to medium risk. Use automated tests, peer review, and deployment monitoring."


@tool
def summarize_incident_severity(user_impact: str, duration_minutes: int) -> str:
    """
    Summarize incident severity from user impact and duration.

    Args:
        user_impact: Description of the user impact.
        duration_minutes: How long the incident lasted.

    Returns:
        A simple severity recommendation.
    """
    impact = user_impact.lower()

    if any(word in impact for word in ["data loss", "security", "payment", "outage"]):
        return "SEV-1 or SEV-2 candidate. Escalate immediately and start incident response."

    if duration_minutes >= 60:
        return "SEV-2 candidate. Long-running impact requires escalation and customer communication."

    if duration_minutes >= 15:
        return "SEV-3 candidate. Track, mitigate, and document follow-up actions."

    return "SEV-4 candidate. Monitor and document if recurring."
