from flask.ext.wtf import Form
from wtforms import TextField, BooleanField , PasswordField ,SubmitField,StringField,validators
from wtforms.validators import DataRequired


class LoginForm(Form):
    
    email = StringField('Email Address', [validators.Length(min=6, max=35)],render_kw={"placeholder": "Email"})
    password = PasswordField('New Password', [
        validators.DataRequired(),
       # validators.EqualTo('confirm', message='Passwords must match')
    ],render_kw={"placeholder": "Password"})
    
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#render_kw={"placeholder": "Email"