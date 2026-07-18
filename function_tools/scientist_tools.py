import pandas as pd
from typing import Dict, List
from crewai.tools import tool

# ---------------------------------------------------------
# Tool 1
# ---------------------------------------------------------

@tool("Recommend ML Problem")
def recommend_ml_problem_type(user_request: str) -> Dict:
    """
    Recommend ML problem type based on the user's request.
    """

    request = user_request.lower()

    mapping = {
        "classification": [
            "classification",
            "predict",
            "churn",
            "fraud",
            "spam",
            "approve",
            "reject"
        ],
        "regression": [
            "price",
            "sales",
            "revenue",
            "amount",
            "cost",
            "forecast value"
        ],
        "clustering": [
            "segment",
            "cluster",
            "group customers"
        ],
        "forecasting": [
            "forecast",
            "future",
            "next month",
            "time series"
        ],
        "anomaly_detection": [
            "anomaly",
            "outlier",
            "fraud detection",
            "abnormal"
        ],
        "recommendation": [
            "recommend",
            "suggest product",
            "movie recommendation"
        ],
        "ranking": [
            "ranking",
            "priority",
            "sort relevance"
        ]
    }

    for problem_type, keywords in mapping.items():
        for keyword in keywords:
            if keyword in request:
                return {
                    "problem_type": problem_type,
                    "reason": f"Detected keyword '{keyword}'."
                }

    return {
        "problem_type": "classification",
        "reason": "Default ML problem."
    }


# ---------------------------------------------------------
# Tool 2
# ---------------------------------------------------------

@tool("Suggest Feature Engineering")
def suggest_feature_engineering(columns: List[str]) -> Dict:
    """
    Suggest feature engineering ideas.
    """

    features = []

    lower_columns = [column.lower() for column in columns]

    if "transaction_date" in lower_columns or "order_date" in lower_columns:
        features.extend([
            "Day of Week",
            "Month",
            "Quarter",
            "Weekend Indicator"
        ])

    if "customer_id" in lower_columns:
        features.extend([
            "Customer Lifetime Value",
            "Purchase Frequency",
            "Days Since Last Purchase"
        ])

    if "amount" in lower_columns or "revenue" in lower_columns:
        features.extend([
            "Rolling Average",
            "Moving Sum",
            "Percentage Change"
        ])

    if not features:
        features = [
            "Normalized Numerical Features",
            "Encoded Categorical Variables",
            "Interaction Features"
        ]

    return {
        "suggested_features": features
    }


# ---------------------------------------------------------
# Tool 3
# ---------------------------------------------------------

@tool("Detect ML Data Risks")
def detect_ml_data_risks(records: list[dict]) -> Dict:
    """
    Detect common ML risks in a dataset.
    """

    df = pd.DataFrame(records)

    risks = []

    if df.duplicated().sum() > 0:
        risks.append("Duplicate rows detected.")

    if df.isnull().sum().sum() > 0:
        risks.append("Missing values detected.")

    high_cardinality = []

    for column in df.columns:

        if df[column].dtype == "object":

            ratio = df[column].nunique() / len(df)

            if ratio > 0.8:
                high_cardinality.append(column)

    if high_cardinality:

        risks.append(
            f"High-cardinality columns: {', '.join(high_cardinality)}"
        )

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:

        if (df[column] < 0).sum() > 0:
            risks.append(
                f"Negative values detected in '{column}'."
            )

    if not risks:

        risks.append(
            "No significant ML data risks detected."
        )

    return {

        "risks": risks

    }
# ---------------------------------------------------------
# Tool 4
# ---------------------------------------------------------

@tool("Recommend Evaluation Metrics")
def recommend_evaluation_metrics(problem_type: str) -> Dict:
    """
    Recommend evaluation metrics.
    """

    metrics = {

        "classification": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1-score",
            "ROC-AUC"
        ],

        "regression": [
            "MAE",
            "RMSE",
            "MSE",
            "R² Score"
        ],

        "clustering": [
            "Silhouette Score",
            "Davies-Bouldin Index"
        ],

        "forecasting": [
            "MAPE",
            "RMSE",
            "MAE"
        ],

        "anomaly_detection": [
            "Precision",
            "Recall",
            "F1-score"
        ],

        "recommendation": [
            "Hit Rate",
            "NDCG",
            "MAP"
        ]

    }

    return {

        "problem_type": problem_type,

        "metrics": metrics.get(
            problem_type,
            ["Accuracy"]
        )

    }


# ---------------------------------------------------------
# Tool 5
# ---------------------------------------------------------

@tool("Create ML Pipeline Plan")
def create_ml_pipeline_plan() -> Dict:
    """
    Create an end-to-end ML pipeline plan.
    """

    return {

        "pipeline": [

            "Data Ingestion",

            "Data Validation",

            "Data Cleaning",

            "Feature Engineering",

            "Train-Test Split",

            "Model Training",

            "Model Evaluation",

            "Model Registry",

            "Inference",

            "Monitoring",

            "Retraining"

        ]

    }