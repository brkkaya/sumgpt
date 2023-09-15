from ctransformers import AutoModelForCausalLM, AutoConfig
from langchain.docstore.document import Document
from data_loader.load_data import DataLoading


class TextEncoder:
    def __init__(self, model_name_or_path: str, model_type: str) -> None:
        self.model_config = AutoConfig.from_pretrained(model_name_or_path)
        self.model_config.config.context_length = 2048
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path, model_type=model_type, config=self.model_config
        )

    def generate_summary(self, prompt: str, is_stream: bool = True):
        for word in self.model(
            prompt=prompt, stream=is_stream, max_new_tokens=2048, stop=["### Instruction", "### Response", "###", "###"]
        ):
            print(word, end="", flush=True)
        pass

    def generate_embedding(self, prompt: str):
        return self.model.embed(prompt)


d: Document = DataLoading().load_pdf_file("data/2309.00071.pdf")

llm = TextEncoder(
    "model/luban-13b.Q4_K_M.gguf",
    model_type="llama",
)
for docs in d:
    # summary_instruction = (
    #     "### Instruction:\n\nI want you to act as a text summarizer to help me create a concise summary of the text I"
    #     " provide. The summary cannot be long but it has to expressing the key points and concepts written in the"
    #     " original text without adding your interpretations. Please ensure that your summary is clear, concise, and"
    #     f" accurately reflects the content. Explain text below:\n{docs.page_content}\n\n### Response:"
    # )
    explanation_instruction = (
        "### Instruction:\n\nI want you to act as a Mathematician and have a PhD in CS. You will explain difficult"
        " concepts. I will provide you article based on mathematics and computer science , and you will respond with a"
        " clear and concise explanation. Your response should include technical language and complex terminology. You"
        " need to explain every formula.You will extract the key-concepts and explain their mathematical formulas."
        " Explain the context in heavily to fill every gap of context. Explain text and equations"
        f" below:\n{docs.page_content}\n\n### Response: \n"
    )

    # llm.generate_summary("What is the meaning of life?")
    print(explanation_instruction)
    llm.generate_summary(explanation_instruction)
    print("\n\n")
