from flask import render_template, redirect, url_for, flash, request, make_response, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from application import app
from application.models import *
from application.forms import *
from application.utils import *
from datetime import timedelta

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
    user = current_user
    reservations = current_user.reservation_made
    
    return render_template('index.html', title='Home', user=user, reservations=reservations)

@app.route('/make-reservation', methods=['GET', 'POST'])
@login_required
def make_reservation():
    form = ReservationForm()

    if form.validate_on_submit():

        reservation = Reservation(
            num_people     = form.num_people.data,
            date           = form.date.data,
            time_start     = form.time_start.data,
            time_end       = (datetime.combine(form.date.data, form.time_start.data) + timedelta(hours=1)).time(),
            reserved_by    = current_user.id,
            table_id       = form.table_id.data
        )

        if datetime.now().date() < form.date.data:
            pass
        else:
            flash("Can't reserve table in the past", 'error')

        if is_collision(reservation):
            flash("This table is already reserved at this time", 'error')
        else:
            db.session.add(reservation)
            db.session.commit()
            flash('Reservation has been made', 'success')
            return redirect(url_for('index'))

    return render_template('make-reservation.html', title='Make Reservation', form=form)

if __name__ == '__main__':
    app.run(debug=True)