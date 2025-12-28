import os
from dotenv import load_dotenv
from openai import OpenAI
from fpdf import FPDF

# 1. Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_pdf_report(analysis_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="AI Recruitment Match Analysis", ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.ln(10) # Add a line break
    
    # Clean up the text for PDF (handling potential encoding issues)
    clean_text = analysis_text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, txt=clean_text)
    
    pdf.output("Career_Match_Report.pdf")
    print("\n✅ PDF Report Generated: Career_Match_Report.pdf")

def analyze_match():
    try:
        with open("cv.txt", "r") as f:
            my_resume = f.read()
        with open("job.txt", "r") as f:
            target_job = f.read()

        print("--- Analyzing Match and Generating Report... ---")

        # General HR Instructions
        instructions = f"""
        You are an expert Executive Recruiter. 
        Analyze the match between this CV and Job Description.
        
        CV: {my_resume}
        JOB: {target_job}

        Provide your response in this exact format:
        1. MATCH SCORE: (Percentage)
        2. TOP MATCHING SKILLS: (List the strongest overlaps)
        3. CRITICAL SKILL GAPS: (What is missing?)
        4. RESUME IMPROVEMENT ADVICE: (Specific tips to get this job)
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": instructions}],
            temperature=0.5
        )

        analysis_result = response.choices[0].message.content
        print(analysis_result)
        
        # Generate the PDF
        create_pdf_report(analysis_result)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_match()
