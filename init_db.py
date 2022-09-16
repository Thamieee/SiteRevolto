import os
import psycopg2

print("creating database connection")
conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user="thamie",
    password="postgres")
    # user=os.environ['DB_USERNAME'],
    # password=os.environ['DB_PASSWORD'])

cur = conn.cursor()

print("creating postgres pgcrypto extension")
cur.execute('CREATE EXTENSION pgcrypto;')
print("dropping previous existing table if exists")
cur.execute('DROP TABLE IF EXISTS users;')
print("creating users table")
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
            'is_admin boolean NOT NULL,'
            'email varchar (150) NOT NULL UNIQUE,'
            'username varchar (150) NOT NULL UNIQUE,'
            'password text NOT NULL,'
            'role varchar (50),'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )
print("commiting changes to database")
conn.commit()
print("process finished, closing connections")
cur.close()
conn.close()