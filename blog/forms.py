from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (BooleanField, PasswordField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(message='Username is required')])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Password is required')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(message='Title field required'),
                                    Length(min=3, max=120,
                                           message='Only 120 characters are allowed')])
    description = TextAreaField('Description',
                                validators=[Length(max=240,
                                                   message='Only 240 characters are allowed')])
    body = TextAreaField('Content',
                         validators=[DataRequired('Content field required')])
    image = FileField('Post Cover', validators=[
                      FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Publish')
