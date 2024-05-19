from langgraph.prebuilt import chat_agent_executor
from e01_setup_llm import setup_llm
from e03_setup_tavily_tool import setup_tavily_tool
from e04_setup_retriever_tool import setup_retriever_tool

from art import *
import os
import pprint

def create_streaming_agent():
    """Create a streaming agent."""
    llm = setup_llm()
    tavily_tool = setup_tavily_tool()
    retriever_tool = setup_retriever_tool()
    tools = [tavily_tool, retriever_tool]
    agent_executor = chat_agent_executor.create_tool_calling_executor(
        llm, tools
    )
    return agent_executor

if __name__ == "__main__":
    # スクリプト名を取得して出力
    script_name = os.path.basename(__file__)
    tprint(script_name)
    
    agent_executor = create_streaming_agent()
    print(f"Streaming Agent: {agent_executor}")