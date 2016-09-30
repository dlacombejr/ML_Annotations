from flask import render_template, url_for, Blueprint, redirect, flash
from flask_login import login_required

baseviews = Blueprint('baseviews', __name__)

@baseviews.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@baseviews.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@baseviews.app_errorhandler(401)
def auth_error(e):
    return redirect(url_for('authviews.login')), 401

@baseviews.route('/')
@baseviews.route('/index')
@login_required
def index():
    title = "Jinja Title"
    return render_template('index.html', title = title, text = 'Hello World!')


@baseviews.route('/new')
@login_required
def new():
    sessions = ['Session 1', 'Session 2', 'Session 3']
    return render_template('new.html', sessions = sessions)