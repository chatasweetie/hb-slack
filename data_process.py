"""Processes data for slack data"""


def checks_if_room(text):
    """Checks to if a request contains a location/room information"""

    possible_locations = set(['ror', 'cos', 'room of requirements', 'chamber of secrets', 'kitchen', 'lecture', 'lecture hall', 'lh'])

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
