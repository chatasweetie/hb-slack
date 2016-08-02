"""Slack Slash Commands for Hackbright"""

import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required t,l.o use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")


@app.route("/")
def index():
    """Homepage Test"""

    return "Hello"

if __name__ == "__main__":

    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
