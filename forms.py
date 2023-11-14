# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectField, URLField, IntegerRangeField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddPetForm(FlaskForm):

    name=StringField('Pet Name', validators=[InputRequired(message='Name field is required')])
    species=SelectField('Pet Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired(message='Species field is required')])
    photo_url=URLField('Pet Photo')
    age=IntegerField('Pet Age', validators=[NumberRange(min=1, max=30, message=None)])
    notes=StringField('Notes')
    available=BooleanField('Is available')