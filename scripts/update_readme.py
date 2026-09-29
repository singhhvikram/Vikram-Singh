import os
import json
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def update_readme():
    with open("profile-data.json", "r") as f:
        profile_data = json.load(f)

    prompt = f"""
    You are an expert technical resume and profile writer.
    Generate a modern, clean, and professional GitHub profile README.md using the following profile details:
    {json.dumps(profile_data, indent=2)}

    Requirements:
    - Include contact badges (LinkedIn, Portfolio, Email).
    - Categorize skills (AI & Automation, Cloud, Process Excellence, AdTech).
    - Summarize current experience and achievements concisely.
    - Output ONLY pure markdown (do not wrap in ```markdown code blocks).
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    with open("README.md", "w") as f:
        f.write(response.text.strip())

if __name__ == "__main__":
    update_readme()
