from crewai import Agent

from function_tools.analyst_tools import (
    profile_dataframe,
    suggest_kpi_metrics,
    generate_dashboard_layout,
    validate_sql_safety,
    explain_query_result,
)


def create_data_analyst_agent(
    llm,
    config,
    step_callback=None,
):
    """
    Creates the Data Analyst Agent.
    """

    return Agent(
        role=config["role"],
        goal=config["goal"],
        backstory=config["backstory"],

        llm=llm,

        verbose=bool(config.get("verbose", True)),

        allow_delegation=bool(
            config.get("allow_delegation", False)
        ),

        max_iter=int(
            config.get("max_iter", 5)
        ),

        max_retry_limit=int(
            config.get("max_retry_limit", 2)
        ),

        respect_context_window=True,

        use_system_prompt=True,

        step_callback=step_callback,

        tools=[
            profile_dataframe,
            suggest_kpi_metrics,
            generate_dashboard_layout,
            validate_sql_safety,
            explain_query_result,
        ],
    )