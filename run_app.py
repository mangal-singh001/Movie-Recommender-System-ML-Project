import subprocess
import time
from pyngrok import ngrok

# 1️⃣ Start Streamlit app
print("Starting Streamlit app...")
streamlit_process = subprocess.Popen(["streamlit", "run", "app.py"])

# 2️⃣ Wait a few seconds for Streamlit to start
time.sleep(5)

# 3️⃣ Start ngrok tunnel
print("Starting ngrok tunnel...")
public_url = ngrok.connect(8501)
print(f"Your public URL is: {public_url}")

# Keep the script running
try:
    streamlit_process.wait()
except KeyboardInterrupt:
    print("Stopping Streamlit and ngrok...")
    streamlit_process.terminate()
    ngrok.disconnect(public_url)
