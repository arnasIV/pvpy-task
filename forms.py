from wtforms import Form, StringField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired

def validate_power(form, field):
    try:
        e_init = float(field.data)
    except ValueError:
        raise ValidationError('Value provided for initial power must be a number.')

def validate_grid(form, field):
    split  = field.data.split()
    if form.binary is not None and form.binary.data:
        cols = len(list(split[0]))
        for i in range(len(split)):
            if not split[i].isnumeric():
                raise ValidationError('Value provided for an element describing a grid must be numeric.')
            arr = list(split[i])
            if len(arr) != cols:
                raise ValidationError('Values provided for elements describing a grid must have the same number of digits.')
    elif form.binary is not None and not form.binary.data:
        for i in range(len(split)):
            if not split[i].isnumeric():
                raise ValidationError('Value provided for an element describing a grid must be numeric.')

class CalculateEnergyForm(Form):
    name = StringField('Name', [DataRequired()])
    binary = BooleanField('Binary')
    power = StringField('Initial Cell Power', [DataRequired(), validate_power])
    grid_input = StringField('Grid Input', [DataRequired(), validate_grid])
