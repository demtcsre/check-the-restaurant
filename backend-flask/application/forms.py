from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, TimeField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
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
    num_people   = IntegerField("Number of People", validators=[DataRequired(), NumberRange(min=1, max=10)])
    table_id     = IntegerField("Table ID", validators=[DataRequired(), NumberRange(min=1, max=10, message="Please enter a valid table ID.")])
    date         = DateField("Date", validators=[DataRequired()])
    time_start   = TimeField("Time Start", validators=[DataRequired()])
    submit       = SubmitField("Book Table")