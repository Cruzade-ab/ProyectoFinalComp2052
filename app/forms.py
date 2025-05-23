from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Formulario para login de usuario
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Formulario para registrar un nuevo usuario
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    
    role = SelectField(
        'Role',
        choices=[('Usuario', 'Usuario'), ('Técnico', 'Técnico')],
        validators=[DataRequired()]
    )

    submit = SubmitField('Register')

# Formulario para cambiar la contraseña del usuario
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')


# Formulario para crear o editar un Ticket
class TicketsForm(FlaskForm):
    asunto = StringField('Ticket title', validators=[DataRequired()])
    descripcion = TextAreaField('Description', validators=[DataRequired()])
    prioridad = SelectField(
        'Prioridad',
        choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')],
        validators=[DataRequired()]
    )
    estado = SelectField(
        'Prioridad',
        choices=[('Abierto', 'Abierto'), ('En proceso', 'En proceso'), ('Cerrado', 'Cerrado')],
        validators=[DataRequired()]
    )
    usuario_id = SelectField(
        'Asignar Usuario',
        choices=[], 
        coerce=int,
        validators=[DataRequired()]
    )
    
    tecnico_id = SelectField(
    'Asignar Técnico',
    choices=[],
    coerce=int,
    
)


    submit = SubmitField('Save')
    
    

class UserEditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField(
        'Role',
        choices=[('Usuario', 'Usuario'), ('Técnico', 'Técnico'), ('Admin', 'Admin')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Guardar cambios')
