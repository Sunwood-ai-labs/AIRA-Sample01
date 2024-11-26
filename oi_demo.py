from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "ollama_chat/gemma2"
interpreter.llm.api_base = "http://localhost:11434"
interpreter.auto_run = True

msg = """
日本語で応答して。適当なPythonのサンプル関数を作業ディレクトリの直下にexampleフォルダに作成してスクリプトを作成して
"""
interpreter.chat(msg.replace('\n', ''), display=True, stream=False)

msg = """
絵文字を使用して作業内容を日本語でコミットして
"""
interpreter.chat(msg.replace('\n', ''), display=True, stream=False)

# interpreter --model ollama/gemma2
