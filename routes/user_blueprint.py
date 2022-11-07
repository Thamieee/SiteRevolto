from flask import Blueprint
from controllers.user_controller import register, profile, confirm_email, login, logout

user_bp = Blueprint("user_bp", __name__)
user_bp.route("/cadastro", methods=["GET", "POST"])(register)
user_bp.route("/profile/<username>", methods=["GET", "PUT"])(profile)
user_bp.route("/confirm/<token>")(confirm_email)
user_bp.route("/login", methods=['GET', 'POST'])(login)
user_bp.route("/logout")(logout)