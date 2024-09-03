import os
import secrets

from flask import current_app
from wtforms.validators import ValidationError

from application import login_manager, jsonify
from application.models import *

def exists_username(form, username):
    user = User.query.filter_by(username = username.data).first()
    if user:
        raise ValidationError("Username already exists. Please use a different username")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def is_collision(reservation):
    target_date = reservation.date
    target_table_id = reservation.table_id
    target_time_start = reservation.time_start

    conflicting_reservations = Reservation.query.filter(
        Reservation.date == target_date,
        Reservation.table_id == target_table_id,
        Reservation.time_start < target_time_start,
        Reservation.time_end > target_time_start
    ).all()

    if conflicting_reservations:
        return True

    return False