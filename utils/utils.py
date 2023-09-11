def generate_summary_prompt(example):
    """Generates a standardized message to prompt the model with an instruction, optional input and a
    'output' field."""
    return f"### Instruction:\n{example['instruction']}\n\n### Response:\n"


def generate_explain_prompt(example):
    """Generates a standardized message to prompt the model with an instruction, optional input and a
    'output' field."""
    return f"### Instruction:\n{example['instruction']}\n\n### Response:\n"
