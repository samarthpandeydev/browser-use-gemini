import asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent

load_dotenv()

# The Google API key is loaded from the .env file

async def main():
    # Initialize the Google Gemini model
    llm = ChatGoogleGenerativeAI(
        model='gemini-1.5-pro',  # Using Google's Gemini model
        temperature=0.0,
    )
    
    # Define a simple task
    task = "Visit example.com and tell me what you see on the page."
    
    print(f"Starting browser-use agent with task: {task}")
    
    # Create the agent
    agent = Agent(task=task, llm=llm)
    
    # Run the agent
    await agent.run()

if __name__ == '__main__':
    asyncio.run(main()) 