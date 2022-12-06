import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SECRET_KEY = os.urandom(32)
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USERNAME = "noreply.revoltosoftware@gmail.com"
# MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
MAIL_PASSWORD = "uyimtytcszuwqcjg"
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEFAULT_SENDER = ("Revolto Software", "noreply.revoltosoftware@gmail.com")
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@192.168.2.59:5432/revolto_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SECURITY_PASSWORD_SALT = os.environ["SECURITY_PASSWORD_SALT"]
SECURITY_PASSWORD_SALT = "revolto_sea_salt"