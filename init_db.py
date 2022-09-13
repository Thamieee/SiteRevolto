import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

cur = conn.cursor()

cur.execute('CREATE EXTENSION pgcrypto;')
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
            'is_admin boolean NOT NULL,'
            'email varchar (150) NOT NULL UNIQUE,'
            'username varchar (150) NOT NULL UNIQUE,'
            'password text NOT NULL,'
            'role varchar (50),'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )