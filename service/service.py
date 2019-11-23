# Creating a Notification Manager class that we wil use to persist
# the NotificationModel instances in an in-memory.

from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from models import NotificationModel
from http_status import HttpStatus
from pytz import utc

class NotificationManager ():
    last_id = 0
    def __init__(self):
        self.notifications = {}

    def insert_notification(self, notification):
        self.__class__.last_id += 1
        notification.id = self.__class__.last_id
        self.notifications[self.__class__.last_id] = notification

    def get_notification(self, id):
        return self.notifications[id]

    def delete_notification(self, id):
        del self.notifications[id]

# Configuring Output fields, we will create a notification_fields dictionary
# that we will use to control the data that we want Flask-RESTful to render
# in our responses when we return NotificationModel instances.

notification_fields = {
    'id': fields.Integer,
    'uri': fields.url('notification_endpoint'),
    'message': fields.String,
    'ttl': fields.Integer,
    'creation_date': fields.DateTime,
    'notification_category': fields.String,
    'displayed_times': fields.Integer,
    'displayed_once': fields.Boolean
}

notification_manager = NotificationManager()
