from langgraph.checkpoint.sqlite import SqliteSaver
from art import *
import os

def setup_memory():
    """Set up the memory for the agent."""
    memory = SqliteSaver.from_conn_string(":memory:")
    return memory

if __name__ == "__main__":
    # スクリプト名を取得して出力
    script_name = os.path.basename(__file__)
    tprint(script_name)
    
    memory = setup_memory()
    print(f"Memory: {memory}")