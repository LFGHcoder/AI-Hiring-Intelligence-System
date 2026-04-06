from utils.llm import call_llm
import json

SYSTEM = """
Generate exactly 3 interview questions:

1 behavioral question
1 cultural fit question
1 technical question

Return ONLY JSON:
{
  "questions": [
    "behavioral question",
    "cultural question",
    "technical question"
  ]
}
"""

def generate_questions(resume: str, job_description: str):
    prompt = f"""
    Resume:
    {resume}

    Job Description:
    {job_description}
    """

    response = call_llm(SYSTEM + "\n\n" + prompt)
    return json.loads(response)