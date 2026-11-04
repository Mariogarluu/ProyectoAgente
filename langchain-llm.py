from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:8b", temperature=0)
response = llm.invoke("Explica RAG en una frase.")
print(response.content)