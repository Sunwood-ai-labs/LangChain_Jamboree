from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI
from langfuse.callback import CallbackHandler
from termcolor import colored
from art import *
import os



# スクリプト名を取得して出力
script_name = os.path.basename(__file__)
tprint(script_name)

# OpenAI APIを使用して言語モデルを初期化
print(colored("言語モデルを初期化中...", "yellow"))
llm = OpenAI(temperature=0)
print(colored("言語モデルの初期化が完了しました！", "green"))

# 会話チェーンを初期化
print(colored("会話チェーンを初期化中...", "yellow"))
conversation = ConversationChain(
    llm=llm, memory=ConversationBufferMemory()
)
print(colored("会話チェーンの初期化が完了しました！", "green"))

# セッション付きのコールバックハンドラーを作成
langfuse_handler = CallbackHandler(session_id="conversation_chain")

# 会話の最初の入力を与える
print(colored("会話を開始します...", "yellow"))
response = conversation.predict(input="こんにちは！", callbacks=[langfuse_handler])
print(colored("ユーザー: こんにちは！", "cyan"))
print(colored(f"アシスタント: {response}", "magenta"))

# 開発者ツールに関する質問をする
input = "素晴らしい朝ごはんを作るにはどうすればいいですか？"
response = conversation.predict(input=input, callbacks=[langfuse_handler])
print(colored(f"ユーザー: {input}", "cyan"))
print(colored(f"アシスタント: {response}", "magenta"))

# 最後の応答を要約するように求める
response = conversation.predict(input="最後の応答を要約してください", callbacks=[langfuse_handler])
print(colored("ユーザー: 最後の応答を要約してください", "cyan"))
print(colored(f"アシスタント: {response}", "magenta"))
print(colored("会話が終了しました。", "green"))