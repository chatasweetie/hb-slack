"""Classes for database to store channels, students, requests & staff"""
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Channel(db.Model):
    """This is an individual Slack Channel"""

    __tablename__ = "channels"

    channel_id = db.Column(db.String(100), primary_key=True, nullable=False)
    cohort_name = db.Column(db.String(100), nullable=False)
    slack_token = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        """Provides useful represenation when printed"""

        return "<Channel cohort_name: {}>".format(self.cohort_name)

    @classmethod
    def gets_channel(cls, channel_id, team_domain, slack_token):
        """returns channel"""

        channel = Channel.query.filter_by(channel_id=channel_id).first()

        if not channel:
            channel = Channel(
                            channel_id=channel_id,
                            cohort_name=team_domain,
                            slack_token=slack_token,
                        )

            db.session.add(channel)
            db.session.commit()

        return channel


class Student(db.Model):
    """This is an individual student"""

    __tablename__ = "students"

    student_id = db.Column(db.String(100), primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    student_slack_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provides useful represenation when printed"""

        return """<Student student_name: {} >""".format(self.student_name)

    @classmethod
    def gets_student(cls, student_id, student_name):
        """returns student"""

        student = Student.query.filter_by(student_id=student_id).first()

        if not student:
            student = Student(
                            student_id=student_id,
                            student_name=student_name,
                        )

            db.session.add(student)
            db.session.commit()

        return student

class Slack_Request(db.Model):
    """This is the individual request for notification"""

    __tablename__ = "slack_requests"

    slack_request_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time_stamp = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.String(5000), nullable=False)
    end_time_stamp = db.Column(db.DateTime, nullable=True)
    student_slack_name = db.Column(db.String(100), nullable=False)

    student_id = db.Column(db.String(100),
                            db.ForeignKey("students.student_id"),
                            nullable=False)

    staff_id = db.Column(db.String(100),
                            db.ForeignKey("staff.staff_id"),
                            nullable=True)

    channel_id = db.Column(db.String(100),
                            db.ForeignKey("channels.channel_id"),
                            nullable=True)

    student = db.relationship("Student", backref="slack_requests")
    staff = db.relationship("Staff", backref="slack_requests")
    channel = db.relationship("Channel", backref="slack_requests")

    def __repr__(self):
        """Provides useful represenation when printed"""

        return """<Slack_Request request_id: {} student: {}
                    staff: {}>""".format(self.slack_request_id,
                                        self.student_id.student_name,
                                        self.staff_id.staff_name)

    @classmethod
    def adds_to_db(cls, student_slack_name, student_id, text, channel_id):
        """adds a student's request to queue"""

        slack_request = Slack_Request(
                            start_time_stamp=datetime.now(),
                            text=text,
                            student_id=student_id,
                            student_slack_name=student_slack_name,
                            channel_id=channel_id,
                        )

        db.session.add(slack_request)
        db.session.commit()


def update_request(slack_request):
    """updates the request to be """
    slack_request.end_time_stamp = datetime.now()
    db.session.add(slack_request)
    db.session.commit()

class Staff(db.Model):
    """This is an individual education team member"""

    __tablename__ = "staff"

    staff_id = db.Column(db.String(100), primary_key=True)
    staff_name = db.Column(db.String(100), nullable=False)
    work_day = db.Column(db.String(15), nullable=True)
    staff_slack_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provides useful represenation when printed"""

        return "<Staff staff_name: {}>".format(self.staff_name)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "postgresql:///hb-slack")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    """will connect to the db"""
    import os
    os.system("dropdb hb-slack")
    print "drop db hb-slack"
    os.system("createdb hb-slack")
    print "create db hb-slack"

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
