from crewai import Crew, Task
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import sqlite3
import pandas as pd


# Disable truncation
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


from agents.demand_forecaster import DemandForecaster
from agents.inventory_manager import InventoryManager
from agents.pricing_optimizer import PricingOptimizer
from agents.insight_analyst import InsightAnalystAgent
from agents.html_converter import HtmlConverterAgent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agent instances
demand_agent = DemandForecaster()
inventory_agent = InventoryManager()
pricing_agent = PricingOptimizer()
insight_agent = InsightAnalystAgent()
html_converter=HtmlConverterAgent()

class ProductRequest(BaseModel):
    product_id: str

class QueryRequest(BaseModel):
    query: str

conn = sqlite3.connect("retail_inventory.db")
demand_df = pd.read_sql_query("SELECT * FROM demand", conn)
inventory_df = pd.read_sql_query("SELECT * FROM inventory", conn)
pricing_df = pd.read_sql_query("SELECT * FROM pricing", conn)
conn.close()

demand_data = demand_df.to_string(index=False)
inventory_data = inventory_df.to_string(index=False)
pricing_data = pricing_df.to_string(index=False)


@app.post("/product/insight", response_class=HTMLResponse)
def product_insight(req: ProductRequest):
    product_id = req.product_id
    conn = sqlite3.connect("retail_inventory.db")
    demand_query = pd.read_sql_query(f"SELECT * FROM demand WHERE product_id = '{product_id}'", conn)
    inventory_query = pd.read_sql_query(f"SELECT * FROM inventory WHERE product_id = '{product_id}'", conn)
    pricing_query = pd.read_sql_query(f"SELECT * FROM pricing WHERE product_id = '{product_id}'", conn)
    conn.close()

    # Task 1: Demand Forecasting Crew
    task_demand = Task(
        description=f"based on this demand data {demand_query.to_string(index=False)}, Analyze demand trends for product ID {product_id}. Provide only structured plain text output.",
        expected_output="Plain text analysis of demand trends.",
        agent=demand_agent
    )

    crew_demand = Crew(
        agents=[demand_agent],
        tasks=[task_demand]
    )
    demand_output = crew_demand.kickoff()
    demand_output = str(demand_output)

    # Task 2: Inventory Management Crew
    task_inventory = Task(
        description=f"based on this demand data {inventory_query.to_string(index=False)}, Analyze inventory status for product ID {product_id}. Provide only structured plain text output.",
        expected_output="Plain text analysis of inventory status.",
        agent=inventory_agent
    )

    crew_inventory = Crew(
        agents=[inventory_agent],
        tasks=[task_inventory]
    )
    inventory_output = crew_inventory.kickoff()
    inventory_output = str(inventory_output)

    # Task 3: Pricing Optimization Crew
    task_pricing = Task(
        description=f"based on this demand data {pricing_query.to_string(index=False)}, Provide pricing strategy recommendations for product ID {product_id}. Provide only structured plain text output.",
        expected_output="Plain text pricing recommendations.",
        agent=pricing_agent
    )

    crew_pricing = Crew(
        agents=[pricing_agent],
        tasks=[task_pricing]
    )
    pricing_output = crew_pricing.kickoff()
    pricing_output = str(pricing_output)

    # Prepare combined input for HTML Converter
    combined_text = (
        f"Demand Analysis:\n{demand_output}\n\n"
        f"Inventory Analysis:\n{inventory_output}\n\n"
        f"Pricing Recommendations:\n{pricing_output}"
    )

    # HTML Converter Crew
    task_html = Task(
        description=f"Convert the following insights into clean, well-structured reading friendly  HTML for frontend display:\n\n{combined_text}",
        expected_output="Well-structured  readable HTML output.",
        agent=html_converter
    )

    crew_html = Crew(
        agents=[html_converter],
        tasks=[task_html]
    )

    final_html = crew_html.kickoff()
    final_html = str(final_html)

    return final_html



@app.post("/chat/query", response_class=HTMLResponse)
async def chatbot_response(request: Request):
    data = await request.json()
    query = data.get("query")

    # Task 1: Run the insight agent first
    task1 = Task(
        description=f"""Analyze the following 3 data and answer this query:
        {query}
        Data:
        demand data:
        {demand_data}
        Inventory data:
        {inventory_data}
        Pricing data:
        {pricing_data}

         You are an expert data analyst.
            Your job is to deeply analyze all 3 data ,that is , demand, inventory, and pricing, and give answers based on user queries.

            Important:
            - If the question is descriptive (like trends, summary, etc.), output clear explanatory text.
            - If the question involves listing data (like product lists, price comparisons, or any table format data), output complete data in **Structured format**.
            - Do not summarize lists. If asked to list products, list all relevant products from the data.
            - DONOT TRUNCATE ANY RESPONSES OR LISTS YOU GENERATE , IF YOU HAVE TO TRUNCATE DO IT SO AFTER 20 LISTINGS

            **IMP* if it involves listing something which is very long  then list only 20 of those , that is list them all (dont use truncate the response  to indicate there are more , just print them)


            The HTML formatting will be handled later by another agent, so no need to format your output.
        """,
        expected_output=f"answer the query : {query} in plain text(neatly and descriptively).",
        agent=insight_agent
    )

    crew_insight = Crew(
        agents=[insight_agent],
        tasks=[task1]
    )

    insight_result = crew_insight.kickoff()
    print("type : ",type(insight_result))

    # Task 2: Pass insight result to the HTML converter
    task2 = Task(
        description=f"""You are an expert at converting data to HTML.

            Instructions:
            - If you receive data, generate appropriate HTML ,or  if you recognise data is tabular the use HTML table with proper headings and rows.
            - If you receive text, wrap it in simple HTML paragraphs.
            - Output only HTML. Do not include any explanation or extra text.
            - Ensure the HTML is clean and readable but also beautiful, suitable for React rendering.
            -  Output plain HTML string only.

            

             example Output:
            <div><p>This is an explanation.</p></div>


             example Output:
            <div><table><thead><tr><th>Product</th><th>Price</th></tr></thead><tbody><tr><td>A</td><td>100</td></tr><tr><td>B</td><td>150</td></tr></tbody></table></div>
                         
            these are just examples ,Do the Structuring of HTML yourself as you see fit for the content 
            -  Output plain HTML string only.

        Data:
        {insight_result}
        """,
        expected_output="Clean, well-structured , beautiful (with inline css) HTML output only.",
        agent=html_converter
    )

    crew_html = Crew(
        agents=[html_converter],
        tasks=[task2]
    )

    final_html = crew_html.kickoff()
    final_html=str(final_html)

    return final_html
