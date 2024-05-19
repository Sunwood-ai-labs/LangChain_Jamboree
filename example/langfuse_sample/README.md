<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/LangChain_Jamboree_Example1.png" width="100%">
</p>

# langfuse_sampleのドキュメント

このディレクトリには、Langfuseライブラリを使用したサンプルコードが含まれています。Langfuseは、LangChainアプリケーションのデバッグとモニタリングを支援するツールです。

## ファイル構成

1. `01_sdk_connection_test.py`: Langfuse SDKとサーバー間の接続をテストするサンプルコード。
2. `02_llm_chain_example.py`: LangChainのLLMチェーンとシーケンシャルチェーンを使用し、Langfuseのコールバックを導入したサンプルコード。
3. `03_conversation_chain_example.py`: LangChainの会話チェーンを使用し、Langfuseのセッション管理機能を導入したサンプルコード。

## 1. `01_sdk_connection_test.py`

このサンプルコードでは、Langfuse SDKとサーバー間の接続をテストします。

1. `CallbackHandler`をインポートし、インスタンスを作成します。
2. `auth_check()`メソッドを呼び出して、接続をテストします。
3. テストの結果を出力します。

## 2. `02_llm_chain_example.py`

このサンプルコードでは、LangChainのLLMチェーンとシーケンシャルチェーンを使用し、Langfuseのコールバックを導入する方法を示します。

1. 必要なライブラリをインポートします。
2. Langfuse SDKとサーバー間の接続をテストします。
3. OpenAIの言語モデルを初期化します。
4. 戯曲のあらすじを生成するLLMチェーンを作成します。
5. 戯曲の批評を生成するLLMチェーンを作成します。
6. あらすじと批評を順番に生成するシーケンシャルチェーンを作成します。
7. チェーンを実行し、Langfuseのコールバックを使用して結果を出力します。

## 3. `03_conversation_chain_example.py`

このサンプルコードでは、LangChainの会話チェーンを使用し、Langfuseのセッション管理機能を導入する方法を示します。

1. 必要なライブラリをインポートします。
2. OpenAIの言語モデルを初期化します。
3. 会話チェーンを初期化します。
4. セッション付きのLangfuseコールバックハンドラーを作成します。
5. 会話の最初の入力を与え、結果を出力します。
6. 開発者ツールに関する質問をし、結果を出力します。
7. 最後の応答を要約するように求め、結果を出力します。

これらのサンプルコードを参考に、Langfuseライブラリを使用してLangChainアプリケーションのデバッグとモニタリングを行うことができます。