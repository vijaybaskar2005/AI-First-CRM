# 🤖 AI-First CRM for Healthcare Professionals (HCP)

An AI-powered Customer Relationship Management (CRM) system built for Medical Representatives (MRs) to efficiently log, manage, and review Healthcare Professional (HCP) interactions using natural language.

Instead of manually filling lengthy forms, the Medical Representative simply chats with the AI Assistant. The LangGraph AI Agent understands the conversation, extracts the interaction details, fills the CRM form automatically, and provides intelligent recommendations.
---
## Live Demo

https://ai-first-crm-beryl.vercel.app/

## GitHub Repository

https://github.com/vijaybaskar2005/AI-First-CRM

---
# 📌 Project Overview

This project was developed as part of the **AIVOA.AI Full Stack Developer (Python + React) Assignment**.

The application combines:

- React Frontend
- FastAPI Backend
- LangGraph AI Agent
- Groq LLM
- MySQL Database

to create an AI-first workflow for pharmaceutical sales representatives.

---

# 🚀 Features

## ✅ AI Assisted Interaction Logging

Medical Representatives describe their doctor visit in natural language.

Example:

> Today I met Dr. Mohan at Apollo Hospital. We discussed Dimma Fever Tablet and JITY-50. The doctor showed positive interest. I provided one sample pack of each product. Follow-up next Tuesday.

The AI automatically extracts:

- Doctor Name
- Hospital
- Date
- Products Discussed
- Sentiment
- Samples Distributed
- Outcomes
- Follow-up Date

and fills the CRM form automatically.

---

## ✅ Read-Only CRM Form

The interaction form cannot be edited manually.

Medical Representatives only review the AI-generated information before saving.

This ensures:

- Consistency
- Reduced manual entry
- AI-first workflow

---

## ✅ AI Generated Follow-up Recommendation

After logging an interaction, the AI immediately recommends the next action.

Example:

- Schedule a follow-up visit
- Collect feedback
- Share product brochure
- Revisit after one week

---

## ✅ AI Interaction Summary

Users can ask:

> Show previous interactions with Dr. Mohan

The AI searches previous interactions and generates a structured summary including:

- Doctor Name
- Total Visits
- Visit Dates
- Products Discussed
- Overall Sentiment
- Recommended Next Action

---

## ✅ AI Email Generator

Users can ask:

> Generate a follow-up email

or

> Generate a follow-up email for Dr. Kumaran regarding Vicks-50 tablets.

The AI generates a professional email including:

- Subject
- Greeting
- Follow-up
- Feedback request
- Stock inquiry
- Signature

---

# 🧠 LangGraph AI Agent

The application uses **LangGraph** to intelligently route every user request to the correct AI Tool.

Workflow:

```
User
   │
   ▼
LangGraph Router
   │
   ├── Log Interaction
   ├── Edit Interaction
   ├── Search Interaction
   ├── Generate Follow-up
   └── Generate Follow-up Email
```

---

# 🛠 LangGraph Tools

## 1️⃣ Log Interaction

Extracts structured CRM data from natural language.

Features:

- Entity Extraction
- Doctor Name Detection
- Product Extraction
- Visit Information
- Sentiment Detection
- Automatic Form Filling

---

## 2️⃣ Edit Interaction

Allows users to modify previously extracted information using natural language.

Example:

> Change the doctor name to Dr. Ram

The AI updates only the requested fields.

---

## 3️⃣ Search Previous Interactions

Searches CRM history and summarizes previous visits.

Includes:

- Number of visits
- Visit dates
- Products discussed
- Sentiment
- Recommended next action

---

## 4️⃣ Generate Follow-up Recommendation

Suggests the best next action after every doctor interaction.

Examples:

- Schedule follow-up
- Collect sample feedback
- Arrange product demo

---

## 5️⃣ Generate Follow-up Email

Creates professional follow-up emails for Healthcare Professionals.

Supports:

- General follow-up emails
- Context-aware emails using doctor name, products, and previous discussion.

---

# 💻 Technology Stack

## Frontend

- React
- Vite
- Axios
- CSS

## Backend

- Python
- FastAPI
- SQLAlchemy
- MySQL

## AI

- LangGraph
- Groq API
- Llama 3.3 70B

---

# 📂 Project Structure

```text
AI-First-CRM
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── main.py
│   │   │
│   │   ├── config/
│   │   │      settings.py
│   │   │
│   │   ├── database/
│   │   │      database.py
│   │   │      dependencies.py
│   │   │
│   │   ├── models/
│   │   │      __init__.py
│   │   │      user.py
│   │   │      hcp.py
│   │   │      interaction.py
│   │   │
│   │   ├── schemas/
│   │   │      user.py
│   │   │      hcp.py
│   │   │      interaction.py
│   │   │      ai.py
│   │   │
│   │   ├── services/
│   │   │      groq_service.py
│   │   │      hcp_service.py
│   │   │      interaction_service.py
│   │   │
│   │   ├── routers/
│   │   │      auth.py
│   │   │      dashboard.py
│   │   │      hcp.py
│   │   │      interaction.py
│   │   │      ai.py
│   │   │
│   │   ├── langgraph/
│   │   │      agent.py
│   │   │
│   │   ├── tools/
│   │   │      classify_intent.py
│   │   │      log_interaction.py
│   │   │      edit_interaction.py
│   │   │      search_interaction.py
│   │   │      summarize_interactions.py
│   │   │      generate_followup.py
│   │   │      generate_followup_email.py
│   │   │      suggest_next_action.py
│   │   │
│   │   └── utils/
│   │
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
│
├── frontend/
│   │
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```


---

# ⚙️ Installation

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend folder.

Example:

```env
APP_NAME=AI-First CRM
DEBUG=False

DB_HOST=
DB_PORT=3306
DB_NAME=
DB_USER=
DB_PASSWORD=

SECRET_KEY=
ALGORITHM=HS256

GROQ_API_KEY=
GROQ_MODEL=llama-3.3-70b-versatile
```

---

# 🎯 Future Improvements

- Email sending integration
- Dashboard & Analytics
- Voice-based interaction logging
- Authentication & Role Management
- Calendar Integration
- Notification System

---

# 👨‍💻 Developer

**S. VijayBaskar**

B.Sc. Computer Science

Python | React | FastAPI | LangGraph | AI Applications

GitHub:

https://github.com/vijaybaskar2005

---

# 📄 License

This project is licensed under the Apache License 2.0.
