from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class NewClientForm(FlaskForm):
    cedula = StringField('Cedula', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    submit = SubmitField('Crear')

class QueryForm(FlaskForm):
    cedula =StringField('Cedula', validators=[DataRequired()])
    submit = SubmitField('Consultar')





# class NewClient(FlaskForm):
#     cliente = StringField('Nuevo Cliente', validators=[DataRequired()])
#     telefono = StringField('Telefono', validators=[DataRequired()])
#     submit = SubmitField('Crear')



# class TodoForm(FlaskForm):
#     description = StringField('Descripción', validators=[DataRequired()])
#     submit = SubmitField('Crear')
