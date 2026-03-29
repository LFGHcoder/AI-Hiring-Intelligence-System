from utils.llm import call_llm
import json

SYSTEM = (
    "You are an expert hiring evaluator. You assess candidate interview answers "
    "based on the job description and score them across multiple dimensions."
)


def evaluate_answers(answers: list, job_description: str):
    prompt = f"""
    Job Description:
    {job_description}

    Candidate Answers:
    {answers}

    Evaluate strictly on:
    - communication (clarity, articulation)
    - leadership (ownership, initiative)
    - problem solving (logic, approach)
    - cultural fit (alignment with role/team)

    Also identify:
    - strengths
    - weaknesses
    - risk flags (red flags or concerns)

    Return ONLY valid JSON:
    {{
      "communication_score": int,
      "leadership_score": int,
      "problem_solving_score": int,
      "cultural_fit_score": int,
      "strengths": [],
      "weaknesses": [],
      "risk_flags": [],
      "final_decision": "Hire/Reject"
    }}
    """

    response = call_llm(f"{SYSTEM}\n\n{prompt}")
    return json.loads(response)