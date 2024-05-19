from langgraph.prebuilt import chat_agent_executor
from e01_setup_llm import setup_llm
from e02_setup_memory import setup_memory
from e03_setup_tavily_tool import setup_tavily_tool
from e04_setup_retriever_tool import setup_retriever_tool
from langchain_core.messages import HumanMessage

from art import *
import os
import pprint
from termcolor import colored

def create_chat_agent():
    """Create a chat agent."""
    llm = setup_llm()
    memory = setup_memory()
    tavily_tool = setup_tavily_tool()
    retriever_tool = setup_retriever_tool()
    tools = [tavily_tool, retriever_tool]
    agent_executor = chat_agent_executor.create_tool_calling_executor(
        llm, tools, checkpointer=memory
    )
    return agent_executor

if __name__ == "__main__":
    
    # スクリプト名を取得して出力
    script_name = os.path.basename(__file__)
    tprint(script_name)
    
    agent_executor = create_chat_agent()
    print(colored(f"Chat Agent: {agent_executor}", "yellow"))
    
    config = {"configurable": {"thread_id": "abc123"}}
   
    response = agent_executor.invoke(
        {"messages": [HumanMessage(content="梅蘭焼きそばのレシピを教えて")]}, config
    )
    print(colored("--------------", "blue"))
    pprint.pprint(response)
    print(colored("--------------", "blue"))
    print(colored(response["messages"][-1].content, "cyan"))