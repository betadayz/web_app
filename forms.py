from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name = StringField('name of Puppy: ')
    

class DelForm(FlaskForm):
    id = IntegerField('Id Number of Puppy to Remove: ')
    submit = SubmitField('Remove Puppy')    