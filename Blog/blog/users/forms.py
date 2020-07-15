from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from wtforms import StringField,TextAreaField,SubmitField, PasswordField, BooleanField ,ValidationError
from wtforms.validators import DataRequired ,Length ,Email ,EqualTo
from flask_login import current_user
from blog.model import User

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(), Length(min=2, max=10)]) 
    email = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password =PasswordField('ConfirmPass' , validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Submit')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already Exists')
    
    def validate_email(self,email):
        email= User.query.filter_by(email=email.data).first()
        if email: 
            raise ValidationError('Email Address already registered')

class LoginForm(FlaskForm):
    email=StringField ('Email' , validators=[DataRequired() , Email()])
    password =PasswordField('Password', validators=[DataRequired()])
    remember= BooleanField('Remember Me')
    submit = SubmitField('Login')   

class UpdateAccountForm(FlaskForm):
    username = StringField('New Username',validators=[DataRequired(), Length(min=2, max=10)]) 
    email = StringField('New Email', validators=[DataRequired(), Email()])
    submit= SubmitField('Update')
    picture= FileField('Update Profile Picture' , validators=[FileAllowed(['jpg','png'])])


    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already Exists')
    
    def validate_email(self,email):
        if email.data != current_user.email:
            email= User.query.filter_by(email=email.data).first()
            if email: 
                raise ValidationError('Email Address already registered')

class RequestResetForm(FlaskForm):
    email=StringField ('Email' , validators=[DataRequired() , Email()])
    submit= SubmitField('Request Password Reset')

    def validate_email(self,email):
        email= User.query.filter_by(email=email.data).first()
        if email is None: 
            raise ValidationError('There is no account with given Email')

class ResetPasswordForm(FlaskForm):
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password =PasswordField('ConfirmPass' , validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Password Reset')
