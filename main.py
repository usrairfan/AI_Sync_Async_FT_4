from dotenv import load_dotenv
import os 
from agents import Agent , Runner, AsyncOpenAI , OpenAIChatCompletionsModel , RunConfig
import asyncio
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# This step is define that How connect with LLM 
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")
#Main step to connect the API with LLM
#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
async def main():
    agent = Agent(
        name = "Translator",
        instructions = "You are a helpful translator. Always translate urdu into english language."
    )

    response = await Runner.run(
        agent,
        input = " -میرا نام اسریٰ عرفان ہے۔ میں جی آئی اے آئی سی میں طالب علم ہوں ",                                                                                        
        run_config = config
    )
    print(response)
asyncio.run(main())    
    