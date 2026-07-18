from function_tools.supervisor_tools import (
    classify_user_request,
    create_agent_work_plan,
    summarize_chat_history,
    validate_final_response_structure,
    estimate_context_usage,
)

from function_tools.analyst_tools import (
    profile_dataframe,
    suggest_kpi_metrics,
    generate_dashboard_layout,
    validate_sql_safety,
    explain_query_result,
)

from function_tools.scientist_tools import (
    recommend_ml_problem_type,
    suggest_feature_engineering,
    detect_ml_data_risks,
    recommend_evaluation_metrics,
    create_ml_pipeline_plan,
)


def register_tools(mcp):
    tools = [
        classify_user_request,
        create_agent_work_plan,
        summarize_chat_history,
        validate_final_response_structure,
        estimate_context_usage,
        profile_dataframe,
        suggest_kpi_metrics,
        generate_dashboard_layout,
        validate_sql_safety,
        explain_query_result,
        recommend_ml_problem_type,
        suggest_feature_engineering,
        detect_ml_data_risks,
        recommend_evaluation_metrics,
        create_ml_pipeline_plan,
    ]

    for tool in tools:
        mcp.tool()(tool)