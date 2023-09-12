from typing import List
from langchain.docstore.document import Document
from ctransformers import AutoModelForCausalLM
from langchain.chains.summarize import load_summarize_chain


class SummarizeDoc:
    def __init__(self, documents: List[Document], model: AutoModelForCausalLM) -> None:
        self.documents = documents
        self.model = model
        self.embedding_history = []
        self.summarize_history = []
        self.map_reduce_chain = load_summarize_chain(llm=model, chain_type="map_reduce")
        self.refine = load_summarize_chain(llm=model, chain_type="refine")

    def summarize_docs(self):
        pass
