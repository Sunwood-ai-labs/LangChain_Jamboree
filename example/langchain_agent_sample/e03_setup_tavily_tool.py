from langchain_community.tools.tavily_search import TavilySearchResults
from art import *
import os


def setup_tavily_tool():
    """Set up the Tavily search tool."""
    search = TavilySearchResults(max_results=2)
    return search

if __name__ == "__main__":
    
    # スクリプト名を取得して出力
    script_name = os.path.basename(__file__)
    tprint(script_name)
    
    tavily_tool = setup_tavily_tool()
    query = "東京の天気は？"
    results = tavily_tool.invoke(query)
    print(f"Query: {query}")
    print(f"Results: {results}")