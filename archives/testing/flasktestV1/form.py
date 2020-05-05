from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SendLogForm(FlaskForm):
    prediction = StringField('Log')
    submit = SubmitField('Submit Message')