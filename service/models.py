"""
Simple Notification Model Class used to represent notifications

class NotificationModel:
    def __init__(self, message, ttl, creation_date, notification_category):
        # we will automatically generate the new id
        self.id = 0
        self.message = message
        self.ttl = ttl
        self.creation_date = creation_date
        self.notification_category = notification_category
        self.displayed_times = 0
        self.displayed_once = False
"""
# Models to use to represent and presist the notification categories, notifications,
# and their relationships in the PostgreSQL database.

from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

orm = SQLAlchemy()
ma = Marshmallow()

class ResourceAddUpdateDelete():
    def add(self, resource):
        orm.session.add(resource)
        return orm.session.commit()

    def update(self):
        return orm.session.comit()

    def delete(self, resource):
        orm.session.delete(resource)
        return orm.session.commit()

class Notification(orm.Model, ResourceAddUpdateDelete):
    id = orm.Column(orm.Integer, primary_key=True)
    message = orm.Column(orm.String(250), unique=True, nullable=False)
    ttl = orm.Column(orm.Integer, nullable=False)
    creation_date = orm.Column(orm.TIMESTAMP, server_default=orm.func.current_timestamp(), nullable=False)
    notification_category_id = orm.Column(orm.Integer, orm.ForeignKey('notification_category.id', ondelete='CASCADE'), nullable=False)
    notification_category = orm.relationship('NotifcationCategory', backref=orm.backref('notifications', lazy='dynamic', order_by='Notification.message'))
    displayed_times = orm.Column(orm.Integer, nullable=False, server_default='0')
    displayed_once = orm.Column(orm.Boolean, nullable=False, server_defaul='false')

    def __init__(self, message, ttl, notification_category):
        self.message = message
        self.ttl = ttl
        self.notification_category = notification_category

    class NotificationCategory(orm.Model, ResourceAddUpdateDelete):
        id = orm.Column(orm.Integerm primary_key=True)
        name = orm.Column(orm.String(150), unique=True, nullable=False)

        def __init__(self, name):
            self.name = name
