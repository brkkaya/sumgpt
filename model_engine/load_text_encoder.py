from ctransformers import AutoModelForCausalLM, AutoConfig


class TextEncoder:
    def __init__(self, model_name_or_path: str, model_type: str) -> None:
        self.model_config = AutoConfig.from_pretrained(model_name_or_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name_or_path, model_type=model_type, config=self.model_config
        )

    def generate_summary(self, prompt: str, is_stream: bool):
        self.model.generate()
        pass

    def generate_embedding(self, prompt: str):
        return self.model.embed(prompt)


llm = TextEncoder(
    "luban-13b.Q4_K_M.gguf",
    model_type="llama",
)
