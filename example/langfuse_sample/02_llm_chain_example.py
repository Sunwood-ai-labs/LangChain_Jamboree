from langchain_openai import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
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

llm = OpenAI(max_tokens=512)
# プロンプトテンプレートを定義
template = """あなたは脚本家です。与えられた戯曲のタイトルに基づいて、あらすじを書くのがあなたの仕事です。
    タイトル: {title}
    脚本家: 上記の戯曲の要約した簡潔な概要はこちらです:"""
prompt_template = PromptTemplate(input_variables=["title"], template=template)
# あらすじを生成するLLMチェーンを作成
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)

# プロンプトテンプレートを定義
template = """あなたはニューヨークタイムズの演劇評論家です。与えられた戯曲のあらすじに基づいて、批評を書くのがあなたの仕事です。
    戯曲のあらすじ:
    {synopsis}
    ニューヨークタイムズの演劇評論家による上記の戯曲の批評:"""
prompt_template = PromptTemplate(input_variables=["synopsis"], template=template)
# 批評を生成するLLMチェーンを作成
review_chain = LLMChain(llm=llm, prompt=prompt_template)

# あらすじと批評を順番に生成するシーケンシャルチェーンを作成
overall_chain = SimpleSequentialChain(
    chains=[synopsis_chain, review_chain],
)

# チェーンを呼び出して実行
print(colored("Generating review...", "yellow"))
review = overall_chain.run("Tragedy at sunset on the beach", callbacks=[langfuse_handler])
print(colored("Review generated successfully!", "green"))
print(colored(review, "magenta"))