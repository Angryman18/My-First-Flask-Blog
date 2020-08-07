from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validiators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
	username = StringField('Username', validiators=[DataRequired(), Length(min=2, max=25)])
	email = StringField('Email', validiators=[DataRequired(), Email()])
    password = PasswordField('Password', validiators=[DataRequired()])
    confirm_pass = PasswordField('Confirm_Password', validiators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class Login(FlaskForm):
    email = StringField('Email', validiators=[DataRequired(), Email()])
    password = PasswordField('Password', validiators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')