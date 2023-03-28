from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import data_required

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[data_required()])
    password = PasswordField('Password', validators=[data_required()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')
