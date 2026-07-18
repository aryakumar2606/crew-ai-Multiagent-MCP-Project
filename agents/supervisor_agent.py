from crewai import Agent


def create_supervisor_agent(
    llm,
    config,
    step_callback=None,
):
    """
    Creates the Supervisor Agent.
    """

    return Agent(
        role=config["role"],
        goal=config["goal"],
        backstory=config["backstory"],

        llm=llm,

        verbose=bool(config.get("verbose", True)),

        allow_delegation=bool(
            config.get("allow_delegation", True)
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

    )

__all__ = ["create_supervisor_agent"]