from ctransformers import AutoModelForCausalLM, AutoConfig
# from utils.utils import generate_explain_prompt, generate_summary_prompt 
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

class TextEncoder:
    def __init__(self, model_name_or_path: str, model_type: str) -> None:
        self.model_config = AutoConfig.from_pretrained(model_name_or_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_name_or_path, model_type=model_type)

    def generate_summary(self, prompt: str):

        self.model.generate()
        pass
# llm = AutoModelForCausalLM.from_pretrained("TheBloke/Luban-13B-GGUF",hf=True, model_file="luban-13b.q4_K_M.gguf",)