import requests
from model import db, Student, Staff, connect_to_db, Channel
import os

TOKEN = raw_input("What is the token for slack? ")
# TOKEN = os.environ.get("SEED_TOKEN")

def seed_channel(token):

    print "seeding channel"

    url = 'https://slack.com/api/team.info?token={}&pretty=1'.format(token)

    response = requests.get(url)

    js = response.json()

    team_id = js['team']['id']
    team_name = js['team']['domain']

    channel = Channel(
                    channel_id=team_id,
                    cohort_name=team_name,
                    )

    db.session.add(channel)
    db.session.commit()


def seed_db(token):
    """seeds the database with student, staff and channel information"""

    url = 'https://slack.com/api/users.list?token={}&pretty=1'.format(token)

    response = requests.get(url)

    js = response.json()

    for person in js['members']:

        person_id = person['id']
        person_name = person['profile']['real_name']
        slack_name = person['name']

        is_staff = raw_input("Is {} a staff member? (y, n or i for ignore) ".format(person_name))

        if is_staff == 'i':
            continue

        if is_staff == 'y':

            staff = Staff.query.filter_by(staff_id=person_id).first()

            work_day = raw_input("What day of the week is {}'s workday? ".format(person_name))

            if work_day == '':
                work_day = False

            if staff:
                staff.work_day = work_day

            else:
                staff = Staff(
                                staff_id=person_id,
                                staff_name=person_name,
                                work_day=work_day,
                                staff_slack_name = slack_name
                            )

            db.session.add(staff)

        else:
            student = Student(
                                student_id=person_id,
                                student_name=person_name,
                                student_slack_name=slack_name
                            )

            db.session.add(student)

    db.session.commit()



if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to DB."

    seed_channel(TOKEN)
    seed_db(TOKEN)
