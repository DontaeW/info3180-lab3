from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Email, length, Regexp

class ContactForm(FlaskForm):     
    name = StringField('Name', validators=[DataRequired(), length(max=150), Regexp(r'^[A-Za-z\s\-]+$')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])