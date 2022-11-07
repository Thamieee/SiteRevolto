from flask import Blueprint
from controllers.user_controller import register, profile, email_verification

user_bp = Blueprint("user_bp", __name__)
user_bp.route("/cadastro", methods=["GET", "POST"])(register)
user_bp.route("/<username>", methods=["GET", "PUT"])(profile)
user_bp.route('/confirm/<token>')(email_verification)