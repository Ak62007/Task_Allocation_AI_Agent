from agent import task_allocation_agent

result = task_allocation_agent(
    user_prompt="Priya: organize your bookshelf and declutter study desk by tomorrow; priority low.",
    model_name="mistralai/Mixtral-8x7B-Instruct-v0.1"
)

print(result)