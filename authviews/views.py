from flask import render_template, url_for, Blueprint, request, redirect, flash
from forms.forms import LoginForm
from models import User
from flask_login import login_user, logout_user


authviews = Blueprint('authviews', __name__, url_prefix='/auth')


@authviews.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash("login successful! Welcome {}".format(user.username))
            return redirect(request.args.get('next') or url_for('baseviews.index'))
        flash('Incorrect username or password.')
    return render_template('login.html', form=form)

@authviews.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('baseviews.index'))