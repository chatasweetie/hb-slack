"""Classes for database to store channels, students, requests & staff"""
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Channel(db.Model):
    """This is an individual Slack Channel"""

    __tablename__ = "channels"

    channel_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cohort_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provides useful represenation when printed"""

        return "<Channel cohort_name: {}>".format(self.cohort_name)


class Student(db.Model):
    """This is an individual student"""

    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provides useful represenation when printed"""

        return """<Student student_name: {} >""".format(self.student_name)


class Request(db.Model):
    """This is the individual request for notification"""

    __tablename__ = "requests"

    request_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time_stamp = db.Column(db.DateTime, nullable=False)
    end_time_stamp = db.Column(db.DateTime, nullable=True)

    student_id = db.Column(db.Integer,
                            db.ForeignKey("student.student_id"),
                            nullable=False)

    staff_id = db.Column(db.Integer,
                            db.ForeignKey("staff.staff_id"),
                            nullable=True)

    channel_id = db.Column(db.Integer,
                            db.ForeignKey("channel.channel_id"),
                            nullable=True)

    def __repr__(self):
        """Provides useful represenation when printed"""

        return """<Request request_id: {} student: {}
                    staff: {}>""".format(self.request_id,
                                        self.student_id.student_name,
                                        self.staff_id.staff_name)


class Staff(db.Model):
    """This is an individual education team member"""

    __tablename__ = "staff"

    staff_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    staff_name = db.Column(db.String(100), nullable=False)
    work_day = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """Provides useful represenation when printed"""

        return "<Staff staff_name: {}>".format(self.staff_name)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "postgresql:///ridemindertest")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    """will connect to the db"""
    import os
    os.system("dropdb hb-slack")
    os.system("createdb hb-slack")

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
