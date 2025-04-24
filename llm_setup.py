from crewai import LLM  
from run_ollama import start_ollama_server

def initialize_llm():
    start_ollama_server()
    return LLM(
    model = 'ollama/gemma3:latest',
    base_url= 'http://localhost:11434', 
    temperature=0.4
    )