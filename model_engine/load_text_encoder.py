from transformers import LlamaForCausalLM, LlamaTokenizer, BitsAndBytesConfig
import torch


class TextEncoder:
    def __init__(self) -> None:
        pass


# #
# model_id = "TheBloke/Llama-2-13B-fp16"


# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True,
# )

# LlamaTokenizer.from_pretrained(model_id)
# LlamaForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map="auto")
