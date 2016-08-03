"""Slack Slash Commands for Hackbright"""

import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from data_process import checks_if_room
from model import Request

app = Flask(__name__)

# Required t,l.o use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")


TOKEN = os.environ.get("TOKEN")


@app.route("/")
def index():
    """Homepage Test"""

    return "Hello"

# TODO:

# route for queuing students
@app.route("/queue", methods=["POST"])
def enqueues():
    """Enqueues Students to Help Queue"""

    token = request.args.get("token")
    channel_id = request.args.get("channel_id")
    user_id = request.args.get("user_id")
    user_name = request.args.get("user_name")
    text = request.args.get("text").lower()
    response_url = request.args.get("response_url")

    if token != TOKEN:
        return "sorry, your not in a regestered slack channel"

    if not checks_if_room(text.split()):
        return "please submit your again, including your location"

    Request.adds_to_db(student_id=student_id, text=text, channel_id=channel_id)

    queue = Request.query.filter_by(end_time_stamp=None).order_by('start_time_stamp').all()



    return "I'm not done yet!"










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
# route for queue opening






###########################################################################################
# route for queue closing





###########################################################################################
# route for messaging students if they haven't been in the queue in x time





###########################################################################################
# route for motivation
# Sarah

# for private messages:
# By default, the response messages sent to commands will only be visible to the user that issued the command (we call these "ephemeral" messages).




###########################################################################################
# route to add channel and bulk add students



###########################################################################################
# route to add staff






if __name__ == "__main__":

    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
