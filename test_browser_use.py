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
    
    # Define a task to scrape data from samarthpandey.com and create a document
    task = '''
    Visit samarthpandey.com and gather comprehensive information about Samarth Pandey.
    Collect details about his background, education, work experience, skills, projects, and any other relevant information.
    Create a well-structured document summarizing all the information you find.
    Make sure to include any notable achievements or interesting facts.
    '''
    
    # Create the agent
    agent = Agent(task=task, llm=llm)
    
    # Run the agent
    await agent.run()

if __name__ == '__main__':
    asyncio.run(main()) 