# StockSage - Personalized Retail Inventory Optimization

**StockSage** is a multi-agent AI system designed to optimize retail inventory management. It leverages advanced AI agents for demand forecasting, inventory management, and pricing optimization, with a focus on real-time predictions, optimization strategies, and data-driven decision-making.

---

## 🚀 Overview

StockSage enhances retail efficiency by integrating intelligent agents that analyze data, predict trends, and recommend actions, ensuring **optimal inventory levels and profitability**.

---

## 🧠 Agents

### 🔹 Demand Forecaster
- Predicts sales trends based on seasonality.
- Identifies top-selling and declining products.
- Detects regional demand variations and flags unusual patterns or outliers.

### 🔹 Inventory Manager
- Suggests optimal safety stock levels and restocking times.
- Identifies slow-moving products.
- Optimizes warehouse space and evaluates supplier performance for delay impacts.

### 🔹 Pricing Optimizer
- Analyzes price elasticity and competitor pricing.
- Recommends dynamic pricing adjustments and discount strategies.
- Simulates pricing change impacts on revenue.

### 🔹 Insight Analyst
- Interprets data from other agents to generate actionable insights.
- Provides clear, human-readable answers or structured formats in response to user queries.

### 🔹 HTML Converter
- Transforms raw outputs from the Insight Analyst into well-structured HTML.
- Ensures seamless rendering on the frontend for an enhanced user experience.

---

## 🏗️ System Model

### **Architecture Overview**
An overview of the system architecture showing how different components and agents interact with each other.

---
![stocksage_system_model](https://github.com/user-attachments/assets/587e90a8-4e53-4da8-addf-230f23b899a0)


## 💻 Technologies Used

### Backend
- **Ollama:** For on-prem LLMs and embedding models.
- **SQLite:** For long-term data storage and memory.
- **FastAPI:** For creating APIs exposing agents' functionalities.
- **Multi-Agent Framework (CrewAI):** For coordinating various agents in a seamless workflow.
- **Python:** The primary language for backend agents and API implementation.

### Frontend
- **React:** For creating interactive user interfaces.
- **JavaScript (JSX):** For frontend logic and rendering dynamic content.

---

## 🧩 LLM Model Used

- **LLaMA 3**  
  Chosen for its strong language understanding and lightweight deployment via Ollama. Runs efficiently on local hardware, making it ideal for real-time multi-agent coordination without relying on cloud-based APIs.

---

## ⚙️ Setup

### Prerequisites

- Ensure **Ollama** is installed.

### Installation Steps

1. **Install Ollama and LLaMA 3**

    ```bash
    ollama pull llama3
    ```

2. **Clone the Repository**

    ```bash
    git clone https://github.com/shashidhar-N-18/StockSage.git
    cd StockSage
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI Application**

    ```bash
    cd backend
    uvicorn main:app --reload
    ```

5. **Run the React Application**

    ```bash
    cd frontend
    npm install
    npm run dev
    ```

---

## 📡 Backend APIs

### 1. **/chat/query - AI Chatbot Endpoint**

- **Description:** Interact with the AI system using natural language queries via the Insight Analyst agent.
- **Method:** POST
- **Request Body Example:**

    ```json
    {
      "query": "What is the expected sales for product XYZ?"
    }
    ```

- **Response:** AI-generated answer (plain text or JSON).

---

### 2. **/product/insight - Product Insights Endpoint**

- **Description:** Provides detailed insights about a specific product.
- **Method:** POST
- **Request Body Example:**

    ```json
    {
      "product_id": "4277"
    }
    ```

- **Response:** Detailed object with product insights.

---

### 3. **/demand/forecast - Demand Forecast Endpoint**

- **Description:** Provides sales predictions and trend analysis.
- **Method:** POST
- **Request Body Example:**

    ```json
    {
      "product_id": "4277",
      "region": "North America"
    }
    ```

- **Response:** Forecasted trends, top-selling/declining products, and outlier flags.

---

### 4. **/inventory/manage - Inventory Management Endpoint**

- **Description:** Offers inventory optimization suggestions.
- **Method:** POST
- **Request Body Example:**

    ```json
    {
      "product_id": "4277"
    }
    ```

- **Response:** Safety stock levels, restocking times, slow-moving alerts, and supplier metrics.

---

### 5. **/pricing/optimize - Pricing Optimization Endpoint**

- **Description:** Provides pricing recommendations.
- **Method:** POST
- **Request Body Example:**

    ```json
    {
      "product_id": "4277",
      "competitor_data": { "price": 49.99 }
    }
    ```

- **Response:** Dynamic pricing, discount strategies, and revenue impact simulations.

---

### 6. **/html/convert - HTML Conversion Endpoint**

- **Description:** Transforms agent outputs into HTML for frontend rendering.
- **Method:** POST
- **Request Body Example:**

    ```json
    {
      "raw_data": "Sales forecast: 500 units next month."
    }
    ```

- **Response:** Well-structured HTML content.

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature-branch
    ```

3. Commit changes:

    ```bash
    git commit -m "Add new feature"
    ```

4. Push to the branch:

    ```bash
    git push origin feature-branch
    ```

5. Submit a pull request.

✅ Ensure you adhere to coding guidelines and include tests.

---

## 📄 License

This project is licensed under the **MIT License** – see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Thanks to the **Ollama** and **CrewAI** communities for their support.
- Special thanks to the open-source contributors of **React** and **FastAPI**.

---
