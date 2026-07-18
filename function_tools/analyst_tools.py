import pandas as pd
import re
from typing import Dict, List
from crewai.tools import tool

# ---------------------------------------------------------
# Tool 1
# ---------------------------------------------------------

@tool("Profile DataFrame")
def profile_dataframe(records: list[dict]) -> Dict:
    """
    Generate a profile of tabular data.

    Args:
        records: List of dictionaries representing table rows.

    Returns:
        Dictionary containing dataset statistics.
    """

    df = pd.DataFrame(records)

    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "column_names": list(df.columns),
        "data_types": {
            column: str(dtype)
            for column, dtype in df.dtypes.items()
        },
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "sample_records": df.head(5).to_dict(orient="records"),
    }
# ---------------------------------------------------------
# Tool 2
# ---------------------------------------------------------

@tool("Suggest KPI Metrics")
def suggest_kpi_metrics(
    domain: str,
    columns: List[str]
) -> Dict:
    """
    Suggest KPIs based on business domain.
    """

    domain = domain.lower()

    kpi_catalog = {

        "ecommerce": [
            "Total Revenue",
            "Average Order Value",
            "Repeat Purchase Rate",
            "Order Cancellation Rate",
            "Monthly Active Customers"
        ],

        "banking": [
            "Loan Approval Rate",
            "Average Account Balance",
            "Fraud Detection Rate",
            "Customer Retention",
            "Transaction Volume"
        ],

        "healthcare": [
            "Patient Count",
            "Average Treatment Cost",
            "Readmission Rate",
            "Bed Occupancy",
            "Average Length of Stay"
        ],

        "education": [
            "Student Enrollment",
            "Course Completion Rate",
            "Average GPA",
            "Attendance Rate",
            "Placement Rate"
        ]

    }

    return {
        "domain": domain,
        "columns": columns,
        "recommended_kpis": kpi_catalog.get(
            domain,
            [
                "Record Count",
                "Growth Rate",
                "Average Value",
                "Unique Users"
            ]
        )
    }


# ---------------------------------------------------------
# Tool 3
# ---------------------------------------------------------

@tool("Generate Dashboard Layout")
def generate_dashboard_layout(
    dashboard_name: str
) -> Dict:
    """
    Suggest dashboard structure.
    """

    return {

        "dashboard_name": dashboard_name,

        "sections": [

            {
                "page": "Overview",
                "chart": "KPI Cards",
                "filters": [
                    "Date",
                    "Region"
                ]
            },

            {
                "page": "Trend Analysis",
                "chart": "Line Chart",
                "filters": [
                    "Month",
                    "Category"
                ]
            },

            {
                "page": "Category Analysis",
                "chart": "Bar Chart",
                "filters": [
                    "Category"
                ]
            },

            {
                "page": "Detailed Records",
                "chart": "Data Table",
                "filters": [
                    "All Columns"
                ]
            }

        ]

    }


# ---------------------------------------------------------
# Tool 4
# ---------------------------------------------------------

@tool("Validate SQL Safety")
def validate_sql_safety(
    query: str
) -> Dict:
    """
    Validate SQL query safety.
    """

    query_upper = query.upper()

    blocked_keywords = [

        "DELETE",
        "UPDATE",
        "DROP",
        "ALTER",
        "INSERT",
        "TRUNCATE",
        "MERGE",
        "CREATE"

    ]

    for keyword in blocked_keywords:

        if re.search(rf"\b{keyword}\b", query_upper):
            return {
                "safe": False,
                "reason": f"{keyword} statements are not allowed."
            }

    warnings = []

    if "SELECT *" in query_upper:
        warnings.append("Avoid using SELECT *.")

    if "WHERE" not in query_upper:
        warnings.append("No WHERE clause detected.")

    if "LIMIT" not in query_upper:
        warnings.append("Consider adding LIMIT.")

    return {
        "safe": True,
        "warnings": warnings
    }


# ---------------------------------------------------------
# Tool 5
# ---------------------------------------------------------

@tool("Explain Query Result")
def explain_query_result(
    metric: str,
    trend: str,
    change_percent: float
) -> str:
    """
    Generate business explanation.
    """

    if trend.lower() == "increasing":

        return (
            f"{metric} increased by {change_percent}%."
            " This indicates positive business growth."
        )

    if trend.lower() == "decreasing":

        return (
            f"{metric} decreased by {abs(change_percent)}%."
            " This may indicate declining performance "
            "or seasonal effects."
        )

    return (
        f"{metric} remained stable with a change of "
        f"{change_percent}%."
    )