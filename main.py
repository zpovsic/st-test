from pyngrok import ngrok

# Setup a tunnel to the streamlit port 80
public_url = ngrok.connect(port='80')
public_url
