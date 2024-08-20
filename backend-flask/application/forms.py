from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, TimeField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from application.utils import exists_username

class SignUpForm(FlaskForm):
    username         = StringField("Username", validators=[DataRequired(), Length(min = 4), exists_username])
    fullname         = StringField("Fullname", validators=[DataRequired(), Length(min = 4)])
    email            = EmailField("Email", validators=[DataRequired(), Length(min = 8), Email(message='Please enter a valid email address.')])
    password         = PasswordField("Password", validators=[DataRequired(), Length(min = 8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message = "Password must match!")])
    submit           = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit   = SubmitField("Login")

class ReservationForm(FlaskForm):
    fullname     = StringField("Fullname", validators=[DataRequired()])
    num_people   = IntegerField("Number of People", validators=[DataRequired()])
    date         = DateField("Date", validators=[DataRequired()])
    time_start   = TimeField("Time Start", validators=[DataRequired()])
    time_end     = TimeField("Time End", validators=[DataRequired()])
    submit       = SubmitField("Book Table")