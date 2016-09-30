import os
from flask import Flask, url_for, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required


class CreateUser(Resource):
    def post(self):
        return {'status': 'success'}
    def get(self):
        return {'status' : 'get success'}

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

#App Config Stuff
app.config['SECRET_KEY'] = '\x87\x95\xaa\x86\x16*3n&x\x85PgY\xc4\xc3\xddl\x05\xad\xa7\x9a(\xd4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tsa.db')
db = SQLAlchemy(app)

from models import User

#Configure Authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
#login_manager.login_view = "authviews.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.User.query.get(int(userid))

api = Api(app)
api.add_resource(CreateUser, '/CreateUser')
# Do extensions first

# Register BluePrints
from baseviews.views import baseviews
app.register_blueprint(baseviews)

from authviews.views import authviews
app.register_blueprint(authviews)

from apis.sessionapis import sessionapis
app.register_blueprint(sessionapis)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
