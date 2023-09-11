from langchain.document_loaders import UnstructuredPDFLoader
from langchain.docstore.document import Document
from langchain.text_splitter import LatexTextSplitter, CharacterTextSplitter


class DataLoading:
    def load_pdf_file(self, file_name: str):
        loader = UnstructuredPDFLoader(file_path=file_name)
        docs = loader.load_and_split(LatexTextSplitter())
        return docs

    def convert_string(self, text: str, metadata=None):
        text_splitted = text.split("\n\n")
        return [Document(page_content=chunk_text, metadata=metadata) for chunk_text in text_splitted]

# d = DataLoading().load_pdf_file("/home/burakkaya/personal_projects/sumgpt/data/2309.00071.pdf")

# print(d)