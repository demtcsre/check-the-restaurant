from application import db
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

class Table(db.Model):
    __tablename__   = "tables"
    id              = db.Column(db.Integer, primary_key = True)
    reserved        = db.Column(db.Boolean, default = False, nullable = False)
    reservation     = db.relationship('Reservation', backref='reservation', lazy=True)
    
class Reservation(db.Model):
    __tablename__  = "reservations"
    id             = db.Column(db.Integer, primary_key = True)
    num_people     = db.Column(db.Integer, nullable = False)
    date           = db.Column(db.Date, nullable = False)
    time_start     = db.Column(db.Time, nullable = False)
    time_end       = db.Column(db.Time, nullable = False)

    reserved_by    = db.Column(db.Integer, db.ForeignKey("users.id"))
    table_id       = db.Column(db.Integer, db.ForeignKey("tables.id"))