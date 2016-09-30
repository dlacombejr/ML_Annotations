from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('Your Username:', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')

class NewAnnotationForm(Form):
    sessionid = StringField('Session ID:', validators=[DataRequired()])
    annotations = StringField('Annotations:', validators=[DataRequired()])
    submit = SubmitField('Save')
