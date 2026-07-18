import math
from typing import Dict, List

from crewai.tools import tool
# ---------------------------------------------------------
# Tool 1
# ---------------------------------------------------------
@tool("Classify User Request")
def classify_user_request(user_query: str) -> Dict:
    """
    Classifies the user's request and recommends which agent
    should handle it.
    """

    query = user_query.lower()

    categories = {
        "dashboard": ["dashboard", "visualization", "chart", "graph"],
        "sql": ["sql", "query", "select", "join", "database"],
        "analytics": ["kpi", "analysis", "analytics", "business", "revenue"],
        "data_science": [
            "machine learning",
            "ml",
            "prediction",
            "classification",
            "regression",
            "clustering",
            "forecast",
            "model"
        ],
        "data_quality": [
            "missing",
            "duplicate",
            "quality",
            "null",
            "outlier"
        ],
        "architecture": [
            "architecture",
            "system design",
            "workflow",
            "pipeline"
        ]
    }

    detected = []

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in query:
                detected.append(category)
                break

    if len(detected) == 0:
        return {
            "intent": "analytics",
            "recommended_agent": "Data Analyst Agent",
            "reason": "General analytics request."
        }

    if len(detected) > 1:
        return {
            "intent": "mixed",
            "recommended_agent": "Both",
            "reason": "Multiple domains detected."
        }

    category = detected[0]

    if category in [
        "analytics",
        "dashboard",
        "sql"
    ]:
        agent = "Data Analyst Agent"

    elif category in [
        "data_science",
        "data_quality"
    ]:
        agent = "Data Scientist Agent"

    else:
        agent = "Supervisor Agent"

    return {
        "intent": category,
        "recommended_agent": agent,
        "reason": f"Detected {category} related request."
    }


# ---------------------------------------------------------
# Tool 2
# ---------------------------------------------------------

@tool("Create Agent Work Plan")
def create_agent_work_plan(intent: str) -> Dict:
    """
    Generates a step-by-step work plan for the agent based on the
    classified intent."""

    plans = {

        "analytics": [
            "Profile dataset",
            "Generate KPIs",
            "Prepare business insights"
        ],

        "dashboard": [
            "Profile dataset",
            "Suggest KPIs",
            "Generate dashboard layout"
        ],

        "sql": [
            "Validate SQL",
            "Execute query safely",
            "Explain results"
        ],

        "data_science": [
            "Detect data quality issues",
            "Recommend ML problem",
            "Suggest evaluation metrics"
        ],

        "mixed": [
            "Data Analyst profiles dataset",
            "Data Analyst generates KPIs",
            "Data Scientist recommends ML",
            "Supervisor combines responses"
        ]
    }

    return {
        "steps": plans.get(
            intent,
            ["Analyze request", "Generate response"]
        )
    }


# ---------------------------------------------------------
# Tool 3
# ---------------------------------------------------------

@tool("Summarize Chat History")
def summarize_chat_history(messages: List[Dict]) -> str:
    """
    Compress chat history into a short summary.
    """

    if len(messages) == 0:
        return "No previous conversation."

    summary = []

    for message in messages[-10:]:

        role = message.get("role", "user")

        content = message.get("content", "")

        summary.append(
            f"{role}: {content[:120]}"
        )

    return "\n".join(summary)


# ---------------------------------------------------------
# Tool 4
# ---------------------------------------------------------

@tool("Validate Final Response Structure")
def validate_final_response_structure(response: str) -> Dict:
    """
    Validates that the final response contains all required sections."""
    required_sections = [

        "Direct Answer",

        "Architecture",

        "Tools Used",

        "Step-by-Step Plan",

        "Risks",

        "Final Recommendation"

    ]

    missing = []

    for section in required_sections:

        if section.lower() not in response.lower():
            missing.append(section)

    return {

        "valid": len(missing) == 0,

        "missing_sections": missing

    }


# ---------------------------------------------------------
# Tool 5
# ---------------------------------------------------------

@tool("Estimate Context Usage")
def estimate_context_usage(
    text: str,
    context_window: int = 8192
) -> Dict:
    """
    Estimates the number of tokens used in the text and the percentage
    of the context window it occupies."""
    estimated_tokens = math.ceil(len(text) / 4)

    percent = round(
        (estimated_tokens / context_window) * 100,
        2
    )

    return {

        "estimated_input_tokens": estimated_tokens,

        "context_window": context_window,

        "usage_percent": percent

    }