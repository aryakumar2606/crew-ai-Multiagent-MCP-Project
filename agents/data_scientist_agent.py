from crewai import Agent

from function_tools.scientist_tools import (
    recommend_ml_problem_type,
    suggest_feature_engineering,
    detect_ml_data_risks,
    recommend_evaluation_metrics,
    create_ml_pipeline_plan,
)


def create_data_scientist_agent(
    llm,
    config,
    step_callback=None,
):
    """
    Creates the Data Scientist Agent.
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
            recommend_ml_problem_type,
            suggest_feature_engineering,
            detect_ml_data_risks,
            recommend_evaluation_metrics,
            create_ml_pipeline_plan,
        ],
    )