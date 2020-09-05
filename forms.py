from wtforms import Form, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class CalculateEnergyForm(Form):
    name = StringField('Name', [DataRequired()])
    binary = BooleanField('Binary')
    power = StringField('Initial Cell Power', [DataRequired()])
    grid_input = StringField('Grid Input', [DataRequired()])
