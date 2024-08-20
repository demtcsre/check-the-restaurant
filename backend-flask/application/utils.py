import os
import secrets

from flask import current_app
from wtforms.validators import ValidationError

from application import login_manager
from application.models import User

def exists_username(form, username):
    user = User.query.filter_by(username = username.data).first()
    if user:
        raise ValidationError("Username already exists. Please use a different username")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))