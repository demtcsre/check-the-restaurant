from application import db, jsonify
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__    = "users"
    id               = db.Column(db.Integer, primary_key = True)
    username         = db.Column(db.String(128), nullable = False)
    fullname         = db.Column(db.String(128), nullable = False)
    email            = db.Column(db.String(128), nullable = False)
    password         = db.Column(db.String(128), nullable = False)

    reservation_made = db.relationship("Reservation", backref="reservation_made", lazy=True)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "fullname": self.fullname,
            "email": self.email
        }
    
    def to_json_reservations(self):
        return {
            "reservations": [r.to_json() for r in self.reservation_made]
        }

class Table(db.Model):
    __tablename__   = "tables"
    id              = db.Column(db.Integer, primary_key = True)
    reservation     = db.relationship('Reservation', backref='reservation', lazy=True)

    def to_json(self):
        return {
            "id": self.id,
            "reservations": [r.to_json() for r in self.reservation]
        }
    
class Reservation(db.Model):
    __tablename__  = "reservations"
    id             = db.Column(db.Integer, primary_key = True)
    num_people     = db.Column(db.Integer, nullable = False)
    date           = db.Column(db.Date, nullable = False)
    time_start     = db.Column(db.Time, nullable = False)
    time_end       = db.Column(db.Time, nullable = False)

    reserved_by    = db.Column(db.Integer, db.ForeignKey("users.id"))
    table_id       = db.Column(db.Integer, db.ForeignKey("tables.id"))

    def to_json(self):
        return {
            "id": self.id,
            "num_people": self.num_people,
            "date": self.date.strftime("%Y-%m-%d"),
            "time_start": self.time_start.strftime("%H:%M"),
            "time_end": self.time_end.strftime("%H:%M"),
            "reserved_by": self.reserved_by,
            "table_id": self.table_id
        }