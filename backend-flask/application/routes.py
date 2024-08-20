from flask import render_template, redirect, url_for, flash, request, make_response, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from application import app
from application.models import *
from application.forms import *
from application.utils import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and password == user.password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html', title="Login", form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():

        user = User(
            username = form.username.data,
            fullname = form.fullname.data,
            email = form.email.data,
            password = form.password.data
        )

        db.session.add(user)
        db.session.commit()
        flash('Account has been made', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', title='SignUp', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/tables', methods=['GET', 'POST'])
@login_required
def tables():
    return render_template('tables.html', title='Tables Available')

@app.route('/my-reservations', methods=['GET', 'POST'])
@login_required
def my_reservations():
    return render_template('reservations.html', title='My Reservations')

@app.route('/make-reservation/<int:table_id>', methods=['GET', 'POST'])
@login_required
def make_reservation(table_id):
    form = ReservationForm()

    if form.validate_on_submit():

        reservation = Reservation(
            fullname   = form.fullname.data,
            num_people = form.num_people.data,
            date       = form.date.data,
            time_start = form.time_start.data,
            time_end   = form.time_end.data,
            table_id   = table_id,
            user_id    = current_user.id
        )

        db.session.add(reservation)
        db.session.commit()
        flash('Reservation has been made', 'success')
        return redirect(url_for('my_reservations'))
    return render_template('make-reservation.html', title='Make Reservation', form=form)

if __name__ == '__main__':
    app.run(debug=True)