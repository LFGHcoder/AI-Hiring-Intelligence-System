from utils.llm import call_llm

SYSTEM = (
    "You draft interview questions for hiring. "
    "Given role and candidate context, output a short list of focused questions."
)


def suggest_questions(text: str) -> str:
    return call_llm(f"{SYSTEM}\n\n{text}")
