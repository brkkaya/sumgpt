from typing import List
from langchain import PromptTemplate
from langchain.docstore.document import Document
from ctransformers import AutoConfig
from langchain.llms import CTransformers
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import LLMChain
from utils.utils import summary_instruction, explanation_instruction


class SummarizeDoc:
    def __init__(self, documents: List[Document], model: CTransformers) -> None:
        self.documents = documents
        self.model = model
        self.embedding_history = []
        self.summarize_history = []
        self.map_reduce_chain = load_summarize_chain(
            llm=model,
            chain_type="map_reduce",
        )
        self.refine = load_summarize_chain(llm=model, chain_type="refine")

    def summarizer_per_doc(self):
        PROMPT = PromptTemplate(template=summary_instruction, input_variables=["text"])

        summary_chain = LLMChain(llm=self.model, prompt=PROMPT)
        output = summary_chain(self.documents)
        return output


from data_loader.load_data import DataLoading

docs = DataLoading().load_pdf_file("./data/2309.00071.pdf")
model_config = AutoConfig.from_pretrained("model/luban-13b.Q4_K_M.gguf")
model_config.model_type = "llama"
model_config.config.context_length = 4096
model = CTransformers(model="model/luban-13b.Q4_K_M.gguf", configs=model_config)
PROMPT = PromptTemplate(template=summary_instruction, input_variables=["text"])
model.stream(PROMPT)
model.generate(PROMPT)
summary = SummarizeDoc(documents=docs[0], model=model)
refine_summary = summary.summarizer_per_doc()
print(refine_summary)
