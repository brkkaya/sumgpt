from langchain.chains import ConversationChain
from ctransformers import AutoModelForCausalLM
from utils.utils import explanation_instruction, summary_instruction
class ChatHistory:
    def __init__(self) -> None:
        pass


class ChatExplanationHistory:
    def __init__(self, model: AutoModelForCausalLM) -> None:
        self.conversation_chain = ConversationChain(llm=model)
        pass


class ChatSummaryHistory:
    def __init__(self, model: AutoModelForCausalLM) -> None:
        self.conversation_chain = ConversationChain(llm=model)
        self.doc_split_indexes = None
        self.current_doc_split_index = 0
    