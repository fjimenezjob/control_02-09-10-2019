from wtforms import Form
from wtforms import validators
from wtforms import HiddenField
from wtforms import NumberField
from wtforms import SelectField


def honeypot_len(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('ATAQUE DE BOT CACA')


class Formulario(Form):

    numero01 = NumberField('Numero01: ', [
        validators.required('Numero requerido!!!'),
        validators.length(min=1, max=100, message='Numero demasiado largo!!!')
    ])

    operación = SelectField('Seleciona la operación:',
        choices=[('+', 'sumar'), ('-', 'restar'), ('x', 'multiplicar'), ('%', 'dividir')])

    numero02 = NumberField('Numero02: ', [
        validators.required('Numero requerido!!!'),
        validators.length(min=1, max=100, message='Numero demasiado largo!!!')

    # trampa honeypot
    honeypot=HiddenField('', [honeypot_len])