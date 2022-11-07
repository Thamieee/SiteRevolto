from datetime import date

from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from models.user_model import User, db
from utils.form_functions import check_user_form
from utils.token import generate_confirmation_token, confirm_token


def register_logic():
    if request.method == "POST":
        data = request.form
        if check_user_form(data):
            user = User(
                email=data["email"],
                username=data["username"],
                password=data["password"],
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
    return render_template("register.html")

def profile_logic(username: str):
    user = User.query.get_or_404(username)
    if request.method == "GET":
        return render_template("user.html", username=username)
    elif request.method == "PUT":
        data = request.form
        user.email = data["email"]
        user.username = data["username"]
        user.password = data["password"]
        db.session.add(user)
        db.session.commit()
        return {"message": f"User {user.username} successfully updated"}

def email_verification_logic(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.is_confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.is_confirmed = True
        user.confirmed_on = date.today()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('app.home'))