#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import openai
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel  # Import BaseModel for request body validation
from langchain_openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_csv_agent

# Load the environment variables from the .env file
load_dotenv()

# Set the OpenAI API key for the library to use
openai.api_key = os.environ.get("OPENAI_API_KEY")

app = FastAPI()

csv_file_path = "data.csv"

# Define a Pydantic model to validate the request body
class PromptRequest(BaseModel):
    prompt: str

# Initialize the agent
llm = OpenAI(temperature=0)
agent = create_csv_agent(
    llm,
    csv_file_path,
    verbose=False,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

@app.get("/")
def read_root(request: Request):
    return {"message": "Bem-vindo ao Sobre Votar em Portugal!"}

@app.post("/prompt")
async def process_prompt(request: PromptRequest):
    prompt = request.prompt  # Extract the prompt from the request body
    response = agent.invoke(prompt)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
