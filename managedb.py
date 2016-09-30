from AnnotationApp import app, db
from models.User import User
from flask_script import Manager

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username = "drcrook", password = "YOURPASSWORD"))
    db.session.add(User(username = "annotator", password = "YOURPASSWORD"))
    db.session.commit()
    print("Initialized the database")

@manager.command
def dropdb():
    db.drop_all()
    print("dropped database")

if __name__ == '__main__':
    manager.run()