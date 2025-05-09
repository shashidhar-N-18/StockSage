# agents/insight_analyst.py
from crewai import Agent
from textwrap import dedent
from langchain_ollama import OllamaLLM
import sqlite3
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Shared LLaMA 3 model using Ollama
llm = OllamaLLM(model="ollama/llama3:latest", timeout=30)

def InsightAnalystAgent():
    
    return Agent(
        role='Insight Analyst',
        goal='Analyze merged data to answer business questions accurately',
        backstory=dedent(f"""
            You are an expert data analyst.
            Your job is to deeply analyze merged data from demand, inventory, and pricing, and give answers based on user queries.
            

            Important:
            - If the question is descriptive (like trends, summary, etc.), output clear explanatory text.
            - If the question involves listing data (like product lists, price comparisons, or any table format data), output complete data in in structured format .
            - Do not summarize lists. If asked to list products, list all relevant products from the data.
            - DONOT TRUNCATE ANY RESPONSES OR LISTS YOU GENERATE , IF YOU HAVE TO TRUNCATE DO IT SO AFTER 20 LISTINGS
                         
            **IMP* if it involves listing something which is very long  then list only 20 of those 
                         **IMP* if it involves listing something which is very long  then list only 20 of those , that is list them all (dont use truncate the response  to indicate there are more , just print them)


            The HTML formatting will be handled later by another agent, so no need to format your output.
        """),
        llm=llm,
        verbose=True
    )
