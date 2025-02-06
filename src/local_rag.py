import os
from langchain_community.llms.ollama import Ollama
from langchain.document_loaders import UnstructuredFileLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.retrieval_qa.base import RetrievalQA

# working directory of folder LLAMA
working_dir = os.path.dirname(os.path.abspath(__file__))
print(working_dir)

llm = Ollama(
    model="llama3.2:1b",
    temperature=0
)

embeddings = HuggingFaceEmbeddings()

def get_answer(file_name, query):
    file_path = f"{working_dir}/{file_name}"

    # loading the document
    loader = UnstructuredFileLoader(file_path)
    documents = loader.load()

    # create text chunks
    text_splitter = CharacterTextSplitter(
                        separator="/n",
                        chunk_size=1000,
                        chunk_overlap=200
                    )
    text_chunks = text_splitter.split_documents(documents)

    # Embeddings into vector from text chunks
    knowledge_base = FAISS.from_documents(text_chunks, embeddings)

    # Chains
    # Combines LLM with FAISS retriever for searching & answering
    qa_chain = RetrievalQA.from_chain_type(
        llm, 
        retriever=knowledge_base.as_retriever()
    )

    # response = {"query": "...", "result": "..."}
    response = qa_chain.invoke({"query": query})

    return response["result"]

