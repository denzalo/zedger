from pathlib import Path
from dotenv import load_dotenv
import os
from flask import Flask, render_template, redirect, request

# Load secrets
secret_path = Path("/etc/secrets/.env")
if secret_path.exists():        # Render
    load_dotenv(dotenv_path=secret_path)
else:                            # Local dev falls back to .env in repo root
    load_dotenv()

app = Flask(__name__)

# Forward the .com domain to the .app domain
@app.before_request
def enforce_primary_domain():
    if request.host and request.host.endswith("zedgerapp.com"):
        url = request.url.replace("zedgerapp.com", "zedger.app")
        return redirect(url, code=301)

# Serve the index page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT
    app.run(host="0.0.0.0", port=port)
