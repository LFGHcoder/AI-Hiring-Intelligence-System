from utils.llm import call_llm

SYSTEM = (
    "You evaluate candidate answers against the role. "
    "Give brief strengths, weaknesses, and a 1–10 score with one-line rationale."
)


def evaluate(text: str) -> str:
    return call_llm(f"{SYSTEM}\n\n{text}")
