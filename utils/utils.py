from langchain.schema import AIMessage, HumanMessage, SystemMessage

explanation_instruction = (
    "### Instruction:\n\nI want you to act as a simple explanation provider for difficult concepts. I will provide a brief"
    " description of a concept, and you will respond with a clear and concise explanation in layman’s terms. Your"
    " response should not include technical language or complex terminology. Instead, you must focus on breaking down"
    " the concept into easy-to-understand language. Explain text below:\n{text}\n\n### Response: "
)


summary_instruction = (
    "### Instruction:\n\nI want you to act as a text summarizer to help me create a concise summary of the text I"
    " provide. The summary cannot be long but it has to expressing the key points and concepts written in the"
    " original text without adding your interpretations. Please ensure that your summary is clear, concise, and"
    " accurately reflects the content. Explain text below:\n{text}\n\n### Response: "
)
