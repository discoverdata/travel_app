import subprocess
import time
import requests
import os

OLLAMA_COMMAND = 'ollama serve'
DEFAULT_OLLAMA_PORT = 11434

def start_ollama_server(timeout: int = 10) -> bool:
    '''Starts Ollama server in the background and checks if it is running.'''
    ollama_process = None

    try:
        # Check if ollama is already running
        try:
            response = requests.get(f'http://localhost:{DEFAULT_OLLAMA_PORT}')
            if response.status_code == 200:
                print("✅ Ollama server is up and running!")
                return True
        except requests.exceptions.ConnectionError:
            pass # Ollama is not running, proceed to start

        ollama_process = subprocess.Popen(
            OLLAMA_COMMAND.split(),
            stdout = subprocess.DEVNULL, 
            stderr = subprocess.DEVNULL
        )
        print(f"🚀 Starting Ollama server with PID {ollama_process.pid}...")
        
        # Wait until the server is up, or timeout
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                response = requests.get(f'http://localhost:{DEFAULT_OLLAMA_PORT}')
                if response.status_code == 200:
                    print("✅ Ollama server is up and running!")
                    return True
            except requests.exceptions.ConnectionError:
                time.sleep(1)
        print(f"⚠️ Ollama server did not become reachable within {timeout} seconds.")
        return False
    
    except Exception as e:
        print(f"❌ Error starting Ollama: {e}")
        return False
    