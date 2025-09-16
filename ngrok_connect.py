from pyngrok import ngrok

# Use integer for port
public_url = ngrok.connect(8501)
print("Your public URL:", public_url)
