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

# TODO:

# route for queuing students
@app.route("/queue", methods=["POST"])
def index():
    """Enqueues Students to Help Queue"""

    # text = request.args.get("text")
    # user_name = request.args.get("user_name")
    # team_id
    # token
    # channel_id



    # JSON needs:
    #     Your URL should respond with a HTTP 200 "OK" status code
    #     example payload: 
    #             {
    #                 "text": "It's 80 degrees right now.",
    #                 "attachments": [
    #                     {
    #                         "text":"Partly cloudy today and tomorrow"
    #                     }
    #                 ]
    #             }
    #     "Ephemeral" responses
    #             {
    #                 "response_type": "in_channel",
    #                 "text": "It's 80 degrees right now.",
    #                 "attachments": [
    #                     {
    #                         "text":"Partly cloudy today and tomorrow"
    #                     }
    #                 ]
    #             }


    # return "Hello"

###########################################################################################
# route for dequeuing students









###########################################################################################
# route for motivation
# Sarah

# for private messages:
# By default, the response messages sent to commands will only be visible to the user that issued the command (we call these "ephemeral" messages).






if __name__ == "__main__":

    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
