import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="tazc54",
                                                                                        DB_PASS="Valto123",
                                                                                        DB_ADDR="127.0.0.1",
                                                                                        DB_NAME="flask_notifications")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
