# agents/html_converter.py
from crewai import Agent
from textwrap import dedent
from langchain_ollama import OllamaLLM

# Shared LLaMA 3 model using Ollama
llm = OllamaLLM(model="ollama/llama3:latest", timeout=30)

def HtmlConverterAgent():
    return Agent(
        role='HTML Converter',
        goal='Convert raw text or JSON data into clean and clean HTML',
        backstory=dedent("""
            You are an expert at converting data to HTML.

            Instructions:
            - If you receive data, generate appropriate HTML ,or  if you recognise data is tabular the use HTML table with proper headings and rows.
            - If you receive text, wrap it in simple HTML paragraphs.
            - Output only HTML. Do not include any explanation or extra text.
            - Ensure the HTML is clean and readable, suitable for React rendering.
            - - Do not output JSON. Output plain HTML string only.
            
            

             example Output:
            <div><p>This is an explanation.</p></div>


             example Output:
            <div><table><thead><tr><th>Product</th><th>Price</th></tr></thead><tbody><tr><td>A</td><td>100</td></tr><tr><td>B</td><td>150</td></tr></tbody></table></div>
                         
            these are just examples ,Do the Structuring of HTML yourself as you see fit for the content 
                         - Do not output JSON. Output plain HTML string only.
        """),
        llm=llm,
        verbose=True
    )
