import os
from dotenv import load_dotenv
from agents import Agent, Runner,FunctionTool, AsyncOpenAI, OpenAIChatCompletionsModel
import requests

# Load environment variables from .env file
load_dotenv()



gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)



# Create an greeting agent with instructions, and model
greeting_agent = Agent(
    name="Greeting Agent",
    instructions="You are a Greeting Agent, Your task is to greet the user with a friendly message, when someone says hi you've reply back with salam from  ali hayat, if someone says bye then say allah hafiz from  ali hayat, when someone asks other than greeting then say Ali is here just for greeting, I can't answer anything else, sorry.",
    model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)
)



# Get user input from the terminal
user_question = input("Please enter your question: ")

# Run the agent with user input and get result
result = Runner.run_sync(greeting_agent, user_question)

# Print the result
print(result.final_output)