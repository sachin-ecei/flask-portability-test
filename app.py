import os
import platform
import sys

import flask
from flask import Flask

app = Flask(__name__)

MESSAGE = os.environ.get("APP_MESSAGE", "Hello from the portability test app!")


@app.route("/")
def index():
    # Environment details make it easy to confirm which machine/setup served the page.
    return (
        f"<h1>{MESSAGE}</h1>"
        f"<p>Python {platform.python_version()} | Flask {flask.__version__}</p>"
        f"<p>{platform.system()} {platform.release()} ({platform.machine()})</p>"
        f"<p>Interpreter: {sys.executable}</p>"
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5000"))
    app.run(host=host, port=port)
