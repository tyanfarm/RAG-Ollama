import os
from langchain_community.llms.ollama import Ollama
from langchain.document_loaders import UnstructuredFileLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import SentenceTransformersTokenTextSplitter  
from langchain.chains.retrieval_qa.base import RetrievalQA

# working directory of folder LLAMA
working_dir = os.path.dirname(os.path.abspath(__file__))

llm = Ollama(
    model="llama3.2:1b",
    temperature=0
)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_answer(file_name, query):
    file_path = f"{working_dir}/{file_name}"

    # loading the document
    loader = UnstructuredFileLoader(file_path)
    documents = loader.load()

    # create text chunks
    # Level 2 - Recursive Character Text Splitting
    text_splitter = RecursiveCharacterTextSplitter(
                        separators=["\n\n", "\n", ".", "?", "!", " ", ""],
                        chunk_size=1024,
                        chunk_overlap=20,
                    )

    text_chunks = text_splitter.split_documents(documents)

    # Print text chunks ----------------------------
    with open("text_chunks_output.txt", "w", encoding="utf-8") as f:
        for i, chunk in enumerate(text_chunks):
            f.write(f"Chunk {i+1}:\n{chunk.page_content}\n{'-'*50}\n")
    # -------------------------------------------------

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

