from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from art import *
import os

def setup_llm():
    """Set up the language model."""
    llm = ChatOpenAI(model="gpt-4o")
    return llm

if __name__ == "__main__":
    # スクリプト名を取得して出力
    script_name = os.path.basename(__file__)
    tprint(script_name)
    
    llm = setup_llm()
    print(f"LLM: {llm}")
    
    # ツールは使わない質問応答
    response = llm.invoke([HumanMessage(content="こんにちは")])
    print("ContentString:", response.content)
    print("ToolCalls:", response.tool_calls)