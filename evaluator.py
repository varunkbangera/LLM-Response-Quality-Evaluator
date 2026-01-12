def evaluate(question, answer):
    result = {}

    # Relevance
    result["relevance"] = 5 if any(word in answer.lower() for word in question.lower().split()) else 3

    # Completeness
    length = len(answer.split())
    if length < 30:
        result["completeness"] = 2
    elif length < 80:
        result["completeness"] = 3
    else:
        result["completeness"] = 5

    # Clarity
    result["clarity"] = 5 if "." in answer and "," in answer else 3

    # Factual Consistency (basic heuristic)
    numbers = any(char.isdigit() for char in answer)
    result["factual_consistency"] = 4 if numbers else 3

    # Hallucination Risk
    risky_terms = ["guaranteed", "100%", "always", "never", "proven", "no doubt"]
    risk = "Low"
    if any(term in answer.lower() for term in risky_terms):
        risk = "High"
    result["hallucination_risk"] = risk

    return result
