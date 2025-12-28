import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the secret API key from your .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_career_path():
    try:
        # 2. Read your Resume (cv.txt)
        with open("cv.txt", "r") as f:
            my_resume = f.read()

        # 3. Read the Job Description (job.txt)
        with open("job.txt", "r") as f:
            target_job = f.read()

        print("--- Analyzing the Bridge between Business and AI... ---")

        # 4. The 'Prompt' - This tells the AI how to think
        instructions = f"""
        You are a Career Strategist specializing in the transition from 
        traditional Business roles to AI & Sustainable Societies roles.

        COMPARE THE FOLLOWING:
        RESUME: {my_resume}
        JOB DESCRIPTION: {target_job}

        PROVIDE THE FOLLOWING IN A CLEAR FORMAT:
        1. SUSTAINABILITY MATCH SCORE: (A percentage 0-100%)
        2. THE BUSINESS ADVANTAGE: (How the candidate's BBA/Western Union background 
           helps them in this specific AI role?)
        3. TECHNICAL GAPS: (List 3 technical skills the candidate should learn 
           during a Master's program like AISS).
        4. PHILOSOPHICAL BRIDGE: (A 2-sentence vision on how this person can 
           make AI more 'human' or 'fair' based on their background).
        """

        # 5. Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Fast, cheap, and smart
            messages=[{"role": "user", "content": instructions}],
            temperature=0.7 # Makes the response more creative/insightful
        )

        # 6. Output the result to your terminal
        print("\n==============================================")
        print("          CAREER BRIDGE AI ANALYSIS           ")
        print("==============================================\n")
        print(response.choices[0].message.content)
        print("\n==============================================")

    except FileNotFoundError:
        print("Error: Make sure cv.txt and job.txt are in the same folder!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_career_path()