from flask import Blueprint
from controllers.user_controller import create, profile

user_bp = Blueprint("user_bp", __name__)
user_bp.route("/cadastro", methods=["GET", "POST"])(create)
user_bp.route("/<username>", methods=["GET", "PUT"])(profile)