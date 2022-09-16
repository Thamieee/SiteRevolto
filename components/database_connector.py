import psycopg2

from flask import flash
from time import sleep

class DatabaseConnector:
    def __init__(self, logger = None):
        self.logger = logger
        self.connection = self.get_connection()

    def get_connection(self):
        try:
            conn = psycopg2.connect(
                host = "localhost",
                database = "flask_db",
                user = "thamie",
                password = "postgres"
            )
        except:
            self.logger.log_error("Falha na conexão com o database")
            self.logger.log_info("Tentativa de reconexão ao database em 5 minutos")
            sleep(300)
            self.connection = self.get_connection()
        return conn

    def verify_form(self, form: dict):
        is_correctly_filled = True
        for key in form:
            if not key:
                flash(f"{key} é um campo obrigatório")
                is_correctly_filled = False
        if form["senha"] != form["confirm_senha"]:
            flash("As senhas não são idênticas")
            is_correctly_filled = False
        return is_correctly_filled

    def register_user(self, form: dict):
        cur = self.connection.cursor()

