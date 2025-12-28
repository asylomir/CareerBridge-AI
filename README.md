# AI Recruitment Matcher & Career Analyst

### **Overview**
The **AI Recruitment Matcher** is a Python-based Decision Support System (DSS) designed to automate and objectify the talent acquisition process. By utilizing Large Language Models (LLMs), the tool performs a deep semantic analysis between a candidate's CV and a specific Job Description, moving beyond simple keyword matching to evaluate "Socio-Technical fit."

### **The Problem & Social Impact**
In a rapidly evolving labor market, professionals often struggle to identify how their transferable skills align with emerging roles. This tool aims to promote **Social Sustainability** by:
1.  **Reducing Bias:** Providing an objective, data-driven match score.
2.  **Bridging Skill Gaps:** Identifying exact technical areas where a candidate needs further training.
3.  **Enhancing Career Mobility:** Helping non-technical professionals transition into tech-centric roles through structured feedback.

---

### **Key Features**
* **Semantic Analysis:** Uses GPT-4o-mini to interpret complex professional experiences.
* **Automated PDF Reporting:** Generates a professional, print-ready document (`Career_Match_Report.pdf`) summarizing the match.
* **Skill Gap Discovery:** Specifically highlights missing competencies to guide educational choices.
* **Resume Optimization:** Provides actionable AI-driven advice to improve resume alignment.

### **Technical Stack**
* **Language:** Python 3.x
* **AI Engine:** OpenAI API (GPT-4o-mini)
* **Document Generation:** `fpdf` library
* **Security:** `python-dotenv` for environment variable protection (API Key management)

---

### **How it Works**
1.  **Input:** The user provides a `cv.txt` (Resume) and a `job.txt` (Job Description).
2.  **Processing:** The script sends a structured prompt to the LLM to analyze the "bridge" between the two documents.
3.  **Output:** The script prints results to the terminal and exports a formatted PDF report.

### **Academic Connection (AISS Application)**
This project was developed as part of my portfolio for the **Erasmus Mundus Master’s in AI for Sustainable Societies (AISS)**. It reflects my commitment to creating tools that bridge the gap between human-centric business management and algorithmic governance.

---

### **Installation & Usage**
1. Clone the repository.
2. Install dependencies: `pip install openai python-dotenv fpdf`
3. Add your OpenAI API key to a `.env` file.
4. Run the program: `python3 career_bridge.py`

*Created by Assyl Umirova*
