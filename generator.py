from together import Together
from load_env import TOGETHER_API_KEY

client = Together(api_key=TOGETHER_API_KEY)

def generate_cover_letter(resume_text, jd_text):
    prompt = f"""
You are a professional career assistant.

Given the following resume and job description, write a tailored cover letter that:

- Highlights the candidate's strengths relevant to the job
- Follows a professional tone
- Is no longer than 300 words
- Starts with a compelling introduction

Resume: 
{resume_text}

Job Description:
{jd_text}

Cover Letter:
"""

    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=600
    )

    return response.choices[0].message.content

