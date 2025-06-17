from together import Together
from load_env import TOGETHER_API_KEY

client = Together(api_key=TOGETHER_API_KEY)

def tailor_resume(resume_text, jd_text):
    prompt = f"""
You are a professional resume reviewer.

Given the resume and job description below, list **only 3–5 specific and concise suggestions** to improve the resume for this job.

Each suggestion must be:
- One sentence only
- Actionable and direct
- Avoid fluff or general comments

Resume:
{resume_text}

Job Description:
{jd_text}

Suggestions (3–5 bullets only):
"""

    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=700
    )

    return response.choices[0].message.content