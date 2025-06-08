from pathlib import Path
from dotenv import load_dotenv
import os
from flask import Flask, render_template

# Load secrets
secret_path = Path("/etc/secrets/.env")
if secret_path.exists():        # Render
    load_dotenv(dotenv_path=secret_path)
else:                            # Local dev falls back to .env in repo root
    load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT
    app.run(host="0.0.0.0", port=port)
