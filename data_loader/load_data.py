# %%
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.docstore.document import Document
from langchain.text_splitter import LatexTextSplitter

class DataLoading:

    def load_pdf_file(file_name: str):
        loader = UnstructuredPDFLoader(file_path=file_name)
        docs = loader.load_and_split(LatexTextSplitter())
        return docs


    def convert_string(text: str, metadata=None):
        text_splitted = text.split("\n\n")
        return [Document(page_content=text_splitted, metadata=metadata)]


    with open("data/test.txt", "r") as f:
        txt = f.read()
        data = convert_string(txt, metadata={"source": "local"})

