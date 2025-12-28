# AI Recruitment Matcher & Career Analyst

### **Project Overview**
The **AI Recruitment Matcher** is a Python-based automation tool designed to streamline the talent acquisition process and provide data-driven insights for job seekers. By leveraging Large Language Models (LLMs), the tool performs a deep semantic analysis between a CV and a Job Description, moving beyond simple keyword matching to evaluate true professional alignment.

### **Who is this for?**
* **For HR Professionals:** Automate the initial screening phase and generate objective, standardized reports to assist in decision-making.
* **For Job Seekers:** Audit your own resume against a target role to identify specific skill gaps and optimize your application before submission.

---

### **Key Features**
* **Semantic Matching Engine:** Evaluates the "hidden" connection between past experiences and new requirements using GPT-4o-mini.
* **Automated PDF Reporting:** Instantly generates a clean, professional `Career_Match_Report.pdf` summarizing the analysis.
* **Gap Identification:** Pinpoints exactly which technical or soft skills are missing from a candidate's profile.
* **Actionable Advice:** Provides a "Roadmap" for how to improve the resume.

### **Technical Stack**
* **Core Logic:** Python 3
* **AI Integration:** OpenAI API 
* **Document Generation:** `fpdf` library
* **Security:** `python-dotenv` (Used to manage environment variables and protect API credentials)

---

### **How it Works**
The system processes data through a three-stage pipeline:
1.  **Ingestion:** Reads raw text from `cv.txt` and `job.txt`.
2.  **Analysis:** The AI compares the two datasets, focusing on skills, responsibility levels, and industry-specific terminology.
3.  **Export:** Results are printed to the console and saved as a formatted PDF report.



### **How to install**
1.  Clone this repository.
2.  Install required libraries: `pip install openai python-dotenv fpdf`
3.  Create a `.env` file and add your `OPENAI_API_KEY`.
4.  Run the application: `python3 career_bridge.py`

---
*Developed as a demonstration of AI-driven automation in Human Resources.*
