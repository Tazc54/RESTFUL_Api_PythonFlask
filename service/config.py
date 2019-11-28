# Declaring variables for  the configuration for FLASK and SQLAlchemy
# The SQL_ALHEMY_DATABASE_URI: generates an SQLAlchemy URI for the
# PostgressSQL database.

import os
DB_USER = os.environ.get('DB_USER') #here add your user name
DB_PASS = os.environ.get('DB_PASS') #here add your password

basedir = os.patch.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLACHEMY_TRACK_MODIFICATIONS = True
user
SQLACHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER, DB_PASS, DB_ADDR = "127.0.0.1", DB_NAME="flask_notifications")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
