# Travel Planner AI Agent

An AI-powered travel planning agent that generates personalized travel itineraries using **Google ADK** and the **Gemini API**, leveraging agentic AI workflows for planning, budgeting, and activity recommendations.

## 🚀 Project Overview

This project demonstrates the design and implementation of an **agentic AI system** capable of:

* Understanding user travel preferences
* Planning end-to-end trips (destinations, activities, budget)
* Coordinating multiple AI agents for structured decision-making
The system is built with a modular architecture and focuses on **clean design, secure API usage, and real-world AI application practices**.

---
## 🧠 Key Features

* Agent-based travel planning using Google ADK
* Gemini API integration for intelligent itinerary generation
* Modular AI agents for planning and support tasks
* Secure environment variable handling
* Extensible design for future enhancements

---

## 🛠 Tech Stack

* **Programming Language:** Python
* **AI / GenAI:** Google ADK, Gemini API
* **Architecture:** Agentic AI (Planner + Supporting Agents)
* **Tools & Libraries:** Python standard libraries
* **Version Control:** Git, GitHub

---

## 🗂 Project Structure

```text
travel-planner-ai-agent/
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
├── travelPlanner/
│   ├── agent.py
│   ├── supportingAgents.py
│   ├── tool.py
│   └── .env.example
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/vaishbyte/travel-planner-ai-agent.git
cd travel-planner-ai-agent
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*(If using `pyproject.toml`, install accordingly.)*

---

## 🔐 Environment Variables

Create a `.env` file inside the `travelPlanner` directory:

```env
GEMINI_API_KEY=your_api_key_here
```

⚠️ **Never commit your `.env` file to GitHub.**

---

## ▶️ How to Run

```bash
python main.py
```

The agent will process user input and generate a personalized travel plan using AI-driven reasoning.

---

## 📊 Use Cases

* Personalized travel itinerary generation
* AI agent orchestration demonstration
* GenAI portfolio project for ML / AI roles
* Learning reference for agent-based AI systems

---

## 📌 Future Enhancements

* Web-based UI for user interaction
* Live API deployment
* Multi-language travel support
* Cost optimization and budget forecasting

---

## 📄 License

This project is for educational and portfolio purposes.

---

## 👤 Author

**Vaishnavi Jaiswal**
Aspiring AI / ML Engineer | Data Science & GenAI Enthusiast

🔗 GitHub: [https://github.com/vaishbyte](https://github.com/vaishbyte)

---

⭐ If you find this project useful, feel free to star the repository!
