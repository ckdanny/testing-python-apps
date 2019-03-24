"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.

"""

from unittest import TestCase
from starter.app import app
from starter.db import db


class BaseTest(TestCase):
    def setUp(self):
        # Make sure database exists, create a new one for it
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context(): # Pretend loaded all the app variables and config and run as app
            # Manually created APP CONTEXT
            # The application context keeps track of the application-level data during a request, CLI command, or other activity.
            # http://flask.pocoo.org/docs/1.0/appcontext/
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app = app.test_client() # Create app instance
        self.app_context = app.app_context # Use for testcase to manually create an app context

        pass

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
        pass
