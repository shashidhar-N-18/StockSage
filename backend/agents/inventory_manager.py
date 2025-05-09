from crewai import Agent
from textwrap import dedent
from langchain_ollama import OllamaLLM

# Shared LLaMA 3 model using Ollama
llm = OllamaLLM(model="ollama/llama3:latest", timeout=30)

def InventoryManager():
    return Agent(
        role='Inventory Manager',
        goal='Optimize inventory levels and ensure stock availability',
        backstory=dedent("""
            You are a highly skilled inventory manager for retail operations.
            Give inventory insights on data in clean way 
            
                         
            - keep the response concise and readable
        """),
        llm=llm,
        verbose=True
    )
