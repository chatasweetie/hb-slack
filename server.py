"""Slack Slash Commands for Hackbright"""

import os

from flask import Flask, request
from flask_debugtoolbar import DebugToolbarExtension
from data_process import checks_if_room, makes_queue_text
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
@app.route("/queue", methods=["GET", "POST"])
def enqueues():
    """Enqueues Students to Help Queue"""

    token = request.form.get("token")
    channel_id = request.form.get("channel_id")
    user_id = request.form.get("user_id")
    user_name = request.form.get("user_name")
    text = request.form.get("text")
    response_url = request.form.get("response_url")

    print "token", token
    print "channel_id", channel_id
    print "user_id", user_id
    print "user_name", user_name
    print "text", text
    print "response_url", response_url

    response = {
                "response_type": "ephemeral",
                }

    #todo: change to a list of possible tokens when we move to mult rooms
    if token != TOKEN:
        response["response_type"] = "ephemeral"
        response["text"] = "sorry, your not in a regestered slack channel"

        return response

    if not checks_if_room(text.split()):
        return "please submit your again, including your location"

    # Request.adds_to_db(student_id=student_id, text=text, channel_id=channel_id)

    # queue = Request.query.filter(Request.end_time_stamp.is_(None)).order_by('start_time_stamp').all()

    response["response_type"] = "in_channel"
    # response["text"] = makes_queue_text(queue)
    response["text"] = 'hi <{}>'.format(user_id)

    if len(queue) > 4:
        pass
        # to poke staff on work day

    return 'hello jessica'




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
