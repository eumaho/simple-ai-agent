
from agent_app.tools import (
    calculate_monthly_cloud_cost,
    check_deployment_risk,
    summarize_incident_severity,
)


def test_calculate_monthly_cloud_cost():
    assert calculate_monthly_cloud_cost.invoke(
        {"hourly_cost": 0.42, "hours_per_day": 24, "days": 30}
    ) == 302.4


def test_database_change_is_high_risk():
    result = check_deployment_risk.invoke({"change_type": "database schema migration"})
    assert "High risk" in result


def test_payment_incident_is_severe():
    result = summarize_incident_severity.invoke(
        {"user_impact": "payment outage", "duration_minutes": 25}
    )
    assert "SEV" in result
