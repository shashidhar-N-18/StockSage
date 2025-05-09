from crewai import Agent
from textwrap import dedent
from langchain_ollama import OllamaLLM

# Shared LLaMA 3 model using Ollama
llm = OllamaLLM(model="ollama/llama3:latest", timeout=30)

def PricingOptimizer():
    return Agent(
        role='Pricing Optimizer',
        goal='Recommend optimal pricing strategies to maximize revenue',
        backstory=dedent("""
            You are an expert in pricing strategy and revenue optimization.
                         give response in clean way

                         

            - keep the response concise and readable
        """),
        llm=llm,
        verbose=True
    )
