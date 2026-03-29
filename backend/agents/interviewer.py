from utils.llm import call_llm
import json

SYSTEM = (
    "You are an AI interviewer. Your job is to generate targeted behavioral "
    "interview questions based on the candidate's resume and the job description."
)


def generate_questions(resume: str, job_description: str):
    prompt = f"""
    Resume:
    {resume}

    Job Description:
    {job_description}

    Generate 5 behavioral interview questions.

    Each question must evaluate:
    - leadership
    - teamwork
    - conflict resolution
    - ownership

    Avoid generic questions. Make them specific to the candidate.

    Return ONLY valid JSON as a list:
    [
      "question 1",
      "question 2",
      "question 3",
      "question 4",
      "question 5"
    ]
    """

    response = call_llm(f"{SYSTEM}\n\n{prompt}")
    return json.loads(response)