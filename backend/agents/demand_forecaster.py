from crewai import Agent
from textwrap import dedent
from langchain_ollama import OllamaLLM

# Shared LLaMA 3 model using Ollama
llm = OllamaLLM(model="ollama/llama3:latest", timeout=30)

def DemandForecaster():
    return Agent(
        role='Demand Forecaster',
        goal='Analyze product demand and predict future trends',
        backstory=dedent("""
            You are an expert demand forecaster for retail products.

           
                         
            - keep the response concise and readable
        """),
        llm=llm,
        verbose=True
    )
