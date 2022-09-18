import psycopg2

from flask import flash
from time import sleep

from utils.schema_functions import enforce_schema, get_users_schema

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

    def insert_to_table(self, table_name: str, table_schema: list,
                        data_to_insert: str) -> None:
        cur = self.connection.cursor()
        cur.execute(f"INSERT INTO {table_name}({table_schema})"
                    + f"VALUES {data_to_insert}")

    def verify_form(self, form: dict) -> bool:
        is_correctly_filled = True
        for key in form:
            if not key:
                flash(f"{key} é um campo obrigatório")
                is_correctly_filled = False
        if form["senha"] != form["confirm_senha"]:
            flash("As senhas não são idênticas")
            is_correctly_filled = False
        return is_correctly_filled

    def register_user(self, form: dict) -> None:
        if self.verify_form(form):
            schema = get_users_schema()
            form = enforce_schema(form=form)
            data_to_insert = []
            for key in form:
                data_to_insert.append(form[key])
            self.insert_to_table(
                table_name="users", table_schema=schema,
                data_to_insert=data_to_insert)
