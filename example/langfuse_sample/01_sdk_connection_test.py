from langfuse.callback import CallbackHandler
from termcolor import colored
from art import *
import os



# スクリプト名を取得して出力
script_name = os.path.basename(__file__)
tprint(script_name)

langfuse_handler = CallbackHandler()

# SDKとサーバーの接続をテスト
print(colored("Testing connection between SDK and server...", "yellow"))
langfuse_handler.auth_check()
print(colored("Connection test successful!", "green"))