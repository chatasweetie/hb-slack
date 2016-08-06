"""Processes data for slack data"""
import requests


def checks_if_room(text):
    """Checks to if a request contains a location/room information"""

    possible_locations = set(['ror', 'cos', 'requirements', 'chamber', 'secrets', 'kitchen', 'lecture', 'lh'])

    for word in text:
        if word in possible_locations:
            return True

    return False


def makes_queue_text(queue):
    """makes a slack queue for response text"""

    response_text = "QUEUE:[ "

    for request in queue:
        response_text += "<@{}>, ".format(request.student_id)

    response_text += ']'

    return response_text


def pokes_staff(TOKEN,):
    """sends a message to staff louge"""
    # channel can be a user id for private messages
    channel_name = "G1XJKJEP2"
    text = "the queue is over 4 people, help!"

    url = 'https://slack.com/api/chat.postMessage?token={}&channel={}&text={}&username=balloonicorn&pretty=1'.format(TOKEN, channel_name, text)
    requests.get(url)
