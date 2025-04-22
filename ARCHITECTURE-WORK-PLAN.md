# 🧠 Job Description Generator – Architecture & Design Document

## 📋 Overview

This is an Agentic AI-powered platform for generating high-quality **Job Descriptions** (JDs) from **natural language prompts** or (eventually) **speech**. It is tailored for the IT/ITeS staffing industry and provides a mobile-friendly UI with multi-provider authentication and outputs the JD in both in-chat display and downloadable `.md` format.

---

## 🧱 High-Level Architecture

```sh

                    +-------------------------+
                    |  🌐 Frontend (Next.js)  |
                    |-------------------------|
                    | - Prompt Input UI       |
                    | - Auth via NextAuth.js  |
                    | - JD display/editor     |
                    +-------------------------+
                                |
                                | HTTPS
                                v
                    +-------------------------+
                    | 🔧 FastAPI Backend       |
                    |-------------------------|
                    | - /api/generate-jd      |
                    | - /api/auth (if needed) |
                    | - /api/generate-md      |
                    +-------------------------+
                                |
                        +-------+--------+
                        |                |
                        v                v
        +----------------------+   +------------------------+
        | 🧠 LangChain Agent   |   | 🛢️ MySQL Database       |
        |----------------------|   |------------------------|
        | - Prompt Parser Tool |   | - Users                |
        | - JD Template Tool   |   | - Prompts              |
        | - JD Composer Tool   |   | - Generated JDs        |
        +----------------------+   +------------------------+
                        |
                        v
          +-----------------------------+
          | 🔮 OpenAI / Claude LLM (API) |
          +-----------------------------+

```

---

## 🧩 Components

### 🌐 Frontend (Free & Mobile-Friendly)
- **Framework**: Next.js (App Router) + Tailwind CSS
- **Auth**: NextAuth.js with:
  - Google
  - Microsoft
  - LinkedIn
  - Credentials (via FastAPI)
- **Prompt Submission**: Rich text area
- **Display JD**: Editable + option to download as `.md` file

---

### 🔧 Backend (Python FastAPI)
- `/api/generate-jd`: Accepts prompt, sends to LangChain agent
- `/api/generate-md`: Converts JD to Markdown format and returns downloadable `.md` file
- `/api/auth`: Optional login route for credentials-based login
- Uvicorn/Gunicorn for serving

---

### 🧠 Agentic AI via LangChain (Python)
A single autonomous agent with modular tools:

#### Agent Tools:
| Tool                  | Responsibility                   |
|-----------------------|----------------------------------|
| `PromptParserTool`    | Extracts role, skills, seniority |
| `JDTemplateTool`      | Chooses IT/ITeS-specific format  |
| `JDComposerTool`      | Calls LLM to generate final JD   |

Can later evolve into a **multi-agent pipeline** using LangGraph.

---

### 🛢️ Database (MySQL)
Tables:
- `users`: OAuth/custom credentials
- `prompts`: Prompt history
- `generated_jds`: JD text + metadata

---

## ☁️ Deployment on AWS (Low-Cost)

| Component         | Service                     | Free Tier?  |
|------------------|------------------------------|-------------|
| Frontend         | Vercel / S3 + CloudFront     | ✅ Yes      |
| Backend          | EC2 (t3.micro) or ECS Fargate| ✅ Yes      |
| DB               | Amazon RDS (MySQL)           | ✅ Yes      |
| JD Files         | S3 (optional for Markdown)   | ✅ Yes      |
| Auth Callback    | Route53 / NextAuth.js        | ✅ Yes      |

---

## 🧰 Tooling Summary

| Area          | Tool/Tech              |
|---------------|------------------------|
| Frontend      | Next.js + Tailwind CSS |
| Auth          | NextAuth.js            |
| Backend       | FastAPI + Uvicorn      |
| Agent         | LangChain (Python)     |
| LLM           | OpenAI / Claude        |
| DB            | MySQL (RDS or Docker)  |
| JD Export     | Markdown `.md` files   |

---

## 🛠️ Development Action Plan

### ✅ Phase 1: Project Setup (MVP)
- [ ] Scaffold `backend/` with FastAPI + LangChain
- [ ] Setup MySQL locally or via RDS Free Tier
- [ ] Integrate OpenAI or Claude API key via env vars
- [ ] Scaffold `frontend/` with Next.js + Tailwind

### ✅ Phase 2: Auth & API
- [ ] Add Google, Microsoft, LinkedIn auth (NextAuth)
- [ ] Add credentials-based login via FastAPI
- [ ] Create `/api/generate-jd` route
- [ ] Implement JD generator agent (LangChain)
- [ ] Save prompts & results in MySQL

### ✅ Phase 3: UI + Features
- [ ] Add mobile-friendly prompt interface
- [ ] Display JD output as editable text
- [ ] Add download as `.md` file (MVP)

### ✅ Phase 4: Stretch Goals
- [ ] Add speech-to-text (Whisper / AWS Transcribe)
- [ ] Add JD versioning or edit history
- [ ] Export to DOCX if needed

### ✅ Phase 5: Deployment
- [ ] Deploy backend to AWS EC2 or ECS
- [ ] Deploy frontend to Vercel or S3
- [ ] Use RDS (MySQL) and optionally S3 for `.md` file storage
- [ ] Set up monitoring and basic logging

---

# 🧠 JD Generator – 5-Day MVP Sprint Plan

This section outlines a focused 5-day sprint to build and deploy the MVP version of the Job Description Generator. The goal is to accept a natural language prompt, generate a Markdown-based JD using an LLM, and display it via a simple web UI. The app will be deployed on an AWS EC2 instance by the end of the sprint.

---

## 🎯 Scope

- ✅ Accept prompt input and return Markdown-based Job Description
- ✅ Display response in a browser with proper formatting
- ✅ Allow download of `.md` file
- ✅ Deploy working app on AWS EC2

---

## ✅ Day 1: Backend Finalization + Prompt Engineering

- [ ] Scaffold FastAPI app (✅ already done)
- [ ] Set up `.env` with:
  ```env
  OPENAI_API_KEY=sk-xxx
  OPENAI_MODEL=gpt-4.1-nano
  OPENAI_TEMPERATURE=0.3
  ```
- [ ] Refine prompt logic in `generate_jd_from_prompt()`:
  - Structure: Naukri-style headings + bullet points
  - Output should be Markdown only (no triple backticks)
- [ ] Define `PromptRequest` and `PromptResponse` models
- [ ] Test `/api/generate-jd` for correct behavior and clean JSON

---

## ✅ Day 2: Web UI – Input Form + Spinner

- [ ] Create Jinja2 template (`index.html`) with:
  - Prompt input `<textarea>`
  - “Generate JD” and “Reset” buttons
  - Spinner: ⏳ Generating...
- [ ] Add `/` GET route to render form
- [ ] Add `/generate` POST route to handle form submission
- [ ] Render Markdown JD using `markdown2` into HTML
- [ ] Basic styling for readability and responsiveness

---

## ✅ Day 3: Display + Markdown Download

- [ ] Render `jd_html` in browser after generation
- [ ] Add `/download` POST route to serve `.md` file
  - Use `Content-Disposition: attachment; filename=job_description.md`
- [ ] Clean up rendering:
  - Strip backticks from LLM output if needed
  - Add box or visual divider around JD output
- [ ] Auto-scroll to result on submit

---

## ✅ Day 4: EC2 Prep + Project Polish

- [ ] Add `README.md` with:
  - Setup steps (venv, .env, API key)
  - Local dev run guide (`uvicorn`)
- [ ] Add `requirements.txt` with only used packages
- [ ] Full integration test with a realistic prompt via UI
- [ ] Minor polish on layout, prompt placeholder, and loading UX
- [ ] Understand the pricing of different LLMs

---

## ✅ Day 5: Deploy to AWS EC2

- [ ] Launch EC2 instance (Ubuntu)
- [ ] SSH in and clone the repo
- [ ] Install Python, create virtualenv, install dependencies
- [ ] Set `.env` with keys and model name
- [ ] Run app with `uvicorn app.main:app --host 0.0.0.0 --port 80`
- [ ] Open EC2 port in security group
- [ ] Access via public IP and verify full flow works end-to-end

---

## 🚀 Outcome

By the end of Day 5, you'll have:
- A working FastAPI backend
- A clean, browser-based UI for JD input + display
- Downloadable `.md` file support
- Your app deployed live on an EC2 instance

---

## ✅ Notes

- Stick to **free tiers** during development (RDS, EC2, Vercel).
- LLM usage is **pay-per-token**, so test with short prompts.
- Markdown generation is fast, readable, and dev-friendly.

---

## 🚀 Future Enhancements

- Company-specific JD memory (via LangChain memory)
- Multi-agent reasoning (LangGraph)
- JD match scoring against candidate resumes
- JD translation/localization for other markets

---

*Built with simplicity, scalability, and minimal cost in mind.*
