from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool

from art import *
import os

def setup_retriever_tool():
    """Set up the retriever tool."""
    loader = WebBaseLoader("https://python.langchain.com/")
    docs = loader.load()
    documents = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200
    ).split_documents(docs)
    vector = FAISS.from_documents(documents, OpenAIEmbeddings())
    retriever = vector.as_retriever()
    retriever_tool = create_retriever_tool(
        retriever,
        "langchain_search",
        "LangChainに関する情報を検索します。LangChainに関する質問がある場合は、このツールを使用する必要があります。",
    )
    return retriever_tool

if __name__ == "__main__":
        
    # スクリプト名を取得して出力
    script_name = os.path.basename(__file__)
    tprint(script_name)
    
    retriever_tool = setup_retriever_tool()
    query = "LangSmithとは？"
    result = retriever_tool.invoke(query)
    print(f"Query: {query}")
    print(f"Result: {result}")