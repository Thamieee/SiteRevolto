from datetime import datetime, date

from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from main import bcrypt
from models.user_model import User, db
from utils.token import generate_confirmation_token, confirm_token
from utils.forms import LoginForm, RegisterForm, ChangePasswordForm
from utils.email import send_email


def register_logic():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.email.data,
            password=form.email.data,
            is_confirmed = False,
            date_added=(date.today())
        )
        db.session.add(user)
        db.session.commit()

        token = generate_confirmation_token(user.email)
        confirm_url = url_for('user.confirm_email', token = token, _external = True)
        html = render_template('user/activate.html', confirm_url = confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)
        login_user(user)
        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for("main.home"))
    return render_template('user/register.html', form=form)

@login_required
def profile_logic(username: str):
    form = ChangePasswordForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email = current_user.email).first()
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('Password successfully changed.', 'success')
            return redirect(url_for('user.profile'))
        else:
            flash('Password change was unsuccessful.', 'danger')
            return redirect(url_for('user.profile'))
    return render_template('user/profile.html', form = form)

def login_logic():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('Welcome.', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form = form)
    return render_template('user/login.html', form = form)

@login_required
def logout_logic():
    logout_user()
    flash('You were logged out.', 'success')
    return redirect(url_for('user.login'))

def confirm_email_logic(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email = email).first_or_404()
    if user.is_confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.is_confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('main.home'))