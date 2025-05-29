from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from dotenv import load_dotenv
import os

load_dotenv()

def get_model(model_name: str):
    """
    Creating the model instance for the task allocation agent.
    """
    if model_name not in ["mistralai/Mixtral-8x7B-Instruct-v0.1", "mistralai/Mistral-7B-Instruct-v0.1"]:
        raise ValueError(f"Unsupported model. Use one of: mistralai/Mixtral-8x7B-Instruct-v0.1, mistralai/Mistral-7B-Instruct-v0.1")
    
    # Create OpenAI provider with OpenRouter configuration
    provider = OpenAIProvider(
        base_url="https://api.together.xyz/v1",
        api_key=os.getenv("TOGETHERAI_API_KEY")
    )
    
    # Create the model with the provider
    llm = OpenAIModel(
        model_name=model_name,
        provider=provider
    )
    return llm


def task_allocation_agent(user_prompt: str, model_name: str):
    import logfire
    import nest_asyncio
    from pydantic_ai import Agent
    from prompt import system_prompt
    from datetime import datetime
    
    time_info = f"\n Current date is {datetime.today()}."
    
    nest_asyncio.apply()
    logfire.configure()
    logfire.instrument_pydantic_ai()
    logfire.info("Task allocation agent started")
    
    task_allocation_agent = Agent(
        model=get_model(model_name),
        system_prompt=f"""{system_prompt} {time_info}""",
    )   
    
    print(f"System prompt: {task_allocation_agent._system_prompts}")
    result = task_allocation_agent.run_sync(user_prompt)
    return result.data