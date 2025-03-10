from wsgiref.validate import validator

from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField
from wtforms import EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    pasыword = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегестрироваться')