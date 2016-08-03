"""Processes data for slack data"""


def checks_if_room(text):
    """Checks to if a request contains a location/room information"""

    possible_locations = set(['ros', 'cos', 'room of requirements', 'chamber of secrets', 'kitchen', 'lecture', 'lecture hall', 'lh'])

    for word in text:
        if word in possible_locations:
            return True

    return False
