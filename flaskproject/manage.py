#!/usr/bin/env python
import os
from flask.ext.script import Manager
import settings
from app import create_app, db
from app.models import User

app = create_app(settings.DevConfig)

manager = Manager(app)

@manager.command
def createdb():
    with app.app_context():
        db.drop_all()
        db.create_all()

@manager.command
def adduser(username):
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt="Confirm: ")
    if password != password2:
        import sys
        sys.exit('Error: Passwords do not match')
    db.create_all()
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print("User {0} was registered successfully".format(username))

if __name__ == '__main__':
    manager.run()
