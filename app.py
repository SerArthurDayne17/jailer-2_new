from flask import Flask, render_template, request
import os

app = Flask(__name__)

TITLE = "அண்ணன் தான்டா Super Star"
DESCRIPTION = "⭐ Click to meet the Super Star! ⭐"


@app.route("/")
def home():
    # Absolute URLs are required so WhatsApp/Facebook/Telegram can show the preview
    base = request.url_root.rstrip("/").replace("http://", "https://")
    return render_template(
        "index.html",
        title=TITLE,
        description=DESCRIPTION,
        image_url=f"{base}/static/anna.jpg",
        page_url=f"{base}/",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), debug=True)
