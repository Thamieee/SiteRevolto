from datetime import date

from flask import render_template, request

from models.user import User, db
from utils.form_functions import check_user_form

def create_logic():
    if request.method == "POST":
        data = request.form
        if check_user_form(data):
            new_user = User(
                email=data["email"],
                username=data["username"],
                password=data["password"],
                date_added=(date.today())
            )
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"User {new_user.username} has been created successfully."}
    return render_template("cadastro.html")

def profile_logic(username: str):
    user = User.query.get_or_404(username)
    if request.method == "GET":
        return render_template("usuario.html", username=username)
    elif request.method == "PUT":
        data = request.form
        user.email = data["email"]
        user.username = data["username"]
        user.password = data["password"]
        db.session.add(user)
        db.session.commit()
        return {"message": f"User {user.username} successfully updated"}