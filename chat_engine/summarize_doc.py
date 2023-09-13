from typing import List
from langchain.docstore.document import Document
from ctransformers import AutoConfig
from langchain.llms import CTransformers
from langchain.chains.summarize import load_summarize_chain


class SummarizeDoc:
    def __init__(self, documents: List[Document], model: CTransformers) -> None:
        self.documents = documents
        self.model = model
        self.embedding_history = []
        self.summarize_history = []
        self.map_reduce_chain = load_summarize_chain(llm=model, chain_type="map_reduce")
        self.refine = load_summarize_chain(llm=model, chain_type="refine")


from data_loader.load_data import DataLoading
docs = DataLoading().load_pdf_file("./data/2309.00071.pdf")
model_config = AutoConfig.from_pretrained("luban-13b.Q4_K_M.gguf")
model_config.model_type = "llama"
model = CTransformers(
            model="luban-13b.Q4_K_M.gguf", configs=model_config
        )

summary = SummarizeDoc(documents=docs,model=model)
refine_summary = summary.refine(docs)
print(refine_summary)

