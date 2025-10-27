# 🧠 AI-Powered Candidate Matching System for HR
*Smart, automated candidate screening using NLP, cosine similarity, and LLMs.*

---

## 📖 Overview
This project helps Human Resources (HR) teams identify the **top 10 candidates** who best align with a given job description or role requirement. By leveraging **Natural Language Processing (NLP)**, **cosine similarity**, **skill matching**, and **Large Language Models (LLMs)**, the system intelligently analyzes and ranks candidate profiles based on relevance and compatibility.

The tool streamlines the hiring process by automating the initial screening phase, reducing manual effort, improving accuracy, and accelerating decision-making. Recruiters can configure the system by providing their LLM API key, selecting the model type (e.g., GPT‑4, Gemini), specifying the folder containing CVs, and choosing the parsing method (NLP or LLM).

---

## 📑 Table of Contents
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Features
- **NLP Resume Parsing**: Extracts and understands job descriptions and candidate resumes.
- **Cosine Similarity**: Measures semantic similarity between job requirements and candidate profiles.
- **Skill Matching Engine**: Compares technical and soft skills for precise alignment.
- **LLM Integration**: Enhances contextual understanding and ranking quality.
- **Top Candidate Ranking**: Generates a ranked list of the 10 most suitable candidates.
- **Configurable User Input**: Supports API key input, model selection, CV folder selection, and parsing method choice.

---

## 📂 Project Structure
```
ai_screener/
│ ├── app/
│   ├── api/
│   │   ├── main.py              # FastAPI entrypoint 
│   │   ├── routes/ 
│   │       ├── screening.py     # CV upload & parsing endpoints, JD input endpoints 
│   │       └── health.py        # Health check
│   ├── core/
│   │   ├── config.py            # Settings (API keys, model selection)
│   │   └── logger.py            # Centralized logging
│   ├── services/ 
│   │   ├── nlp/ 
│   │   │   ├── extract_skills.py 
│   │   │   ├── get_skills.py 
│   │   │   ├── jz_skill_patterns.jsonl 
│   │   │   └── embeddings.py 
│   │   ├── llm/ 
│   │   │   ├── extract_skills_llm.py 
│   │   │   ├── llm_ranking.py 
│   │   │   └── prompt_templates.py 
│   │   ├── get_data.py		 # Read .pdf and .docx CVs from the selected folders 
│   │   └── screening.py         # Orchestrates CV ↔ JD matching 
│   ├── models/ 
│   │   └── schemas.py           # Pydantic models 
│   └── init.py 
├── frontend/ 
│   ├── index.html 
│   ├── styles.css 
│   └── app.js 
├── tests/ 
│   ├── test_api.py 
│   ├── test_nlp_extract_skills.py 
│   └── test_extract_skills_llm.py 
├── requirements.txt 
├── Dockerfile 
├── docker-compose.yml 
└── README.md
```
## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohsinraza2999/AI-Screener.git
   cd ai-screener
   ```
2. **Create a virtual environment & install dependencies**
  ```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
  ```
3. **🚀 Usage**
  Run the FastAPI server
    ```Bash
    uvicorn app.api.main:app --reload```
  **Example Workflow**
- Provide your LLM API key and select the model (e.g., GPT‑4, Gemini).
- Upload candidate CVs (.pdf or .docx) to the designated folder.
- Submit a job description via the API or frontend.
- Receive a ranked list of the top 10 candidates.

4. **Run with Docker (optional)**
   ```docker-compose up --build```
3# 🛠 Tech Stack
- Backend: FastAPI, Uvicorn, Python
- NLP: spaCy, Sentence-Transformers, cosine similarity
- LLM Integration: LangChain, LangChain-OpenAI
- Frontend: HTML, CSS, JavaScript
- Infrastructure: Docker, Docker Compose, CI/CD pipeline
- Testing: Pytest
- Other: Logging middleware, embeddings, config managemen

## 🤝 Contributing
Contributions are welcome!
- Fork the repository
- Create a new branch (git checkout -b feature/your-feature)
- Commit your changes (git commit -m "Add new feature")
- Push to your branch (git push origin feature/your-feature)
- Open a Pull Request

## 📜 License
This project is licensed under the MIT License.
See the LICENSE file for details
This `README.md` is **ready to publish** — it’s professional, self-contained, and developer-friendly.  

Would you like me to also create a **shorter, recruiter-friendly version** of the README (less technical, more business-focused) for non-developer stakeholders?

