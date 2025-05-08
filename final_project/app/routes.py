from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms import TicketForm, ChangePasswordForm
# from app.forms import TicketForm, ChangePasswordForm
from app.models import db, Ticket, User, Ticket

# Blueprint principal que maneja el dashboard, gestión de tickets y cambio de contraseña
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Página de inicio pública (home).
    """
    return render_template('index.html')

@main.route('/cambiar-password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    """
    Permite al usuario autenticado cambiar su contraseña.
    """
    form = ChangePasswordForm()

    if form.validate_on_submit():
        # Verifica que la contraseña actual sea correcta
        if not current_user.check_password(form.old_password.data):
            flash('Current password is incorrect.')  # 🔁 Traducido
            return render_template('cambiar_password.html', form=form)

        # Actualiza la contraseña y guarda
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('✅ Password updated successfully.')  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    return render_template('cambiar_password.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    """
    Panel principal del usuario. Muestra los tickets si no es estudiante.
    """
    if current_user.role.name == 'Usuario': # Change this for your project
        tickets = Ticket.query.all()
    else:
        tickets = Ticket.query.filter_by(tecnico_id=current_user.id).all()

    return render_template('dashboard.html', tickets=tickets)

@main.route('/tickets', methods=['GET', 'POST'])
@login_required
def tickets():
    """
    Permite crear un nuevo ticket. Solo disponible para tecnico o admins.
    """
    form = TicketForm()
    if form.validate_on_submit():
        ticket = Ticket(
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            tecnico_id=current_user.id
        )
        db.session.add(ticket)
        db.session.commit()
        flash("Ticket created successfully.")  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    return render_template('ticket_form.html', form=form)

@main.route('/tickets/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_ticket(id):
    """
    Permite editar un ticket existente. Solo si es admin o el tecnico dueño.
    """
    ticket = Ticket.query.get_or_404(id)

    # Validación de permisos
    if current_user.role.name not in ['Admin', 'Técnico'] or (
        ticket.tecnico_id != current_user.id and current_user.role.name != 'Admin'):
        flash('You do not have permission to edit this course.')  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    form = TicketForm(obj=ticket)

    if form.validate_on_submit():
        ticket.titulo = form.titulo.data
        ticket.descripcion = form.descripcion.data
        db.session.commit()
        flash("Ticket updated successfully.")  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    return render_template('ticket_form.html', form=form, editar=True)

@main.route('/tickets/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_ticket(id):
    """
    Elimina un ticket si el usuario es admin o su tecnico creador.
    """
    ticket = Ticket.query.get_or_404(id)

    if current_user.role.name not in ['Admin', 'Técnico'] or (
        ticket.tecnico_id != current_user.id and current_user.role.name != 'Admin'):
        flash('You do not have permission to delete this course.')  # 🔁 Traducido
        return redirect(url_for('main.dashboard'))

    db.session.delete(ticket)
    db.session.commit()
    flash("Ticket deleted successfully.")  # 🔁 Traducido
    return redirect(url_for('main.dashboard'))

@main.route('/usuarios')
@login_required
def listar_usuarios():
    if current_user.role.name != 'Admin':
        flash("You do not have permission to view this page.")
        return redirect(url_for('main.dashboard'))

    # Obtener instancias completas de usuarios con sus roles (no usar .add_columns)
    usuarios = User.query.join(User.role).all()

    return render_template('usuarios.html', usuarios=usuarios)


@main.route('/tickets', methods=['GET'])
def listar_tickets():
    """
    Retorna una lista de tickets en formato JSON.
    """
    try:
        # Obtener todos los tickets de la base de datos
        tickets = Ticket.query.all()

        # Formatear los datos en una lista de diccionarios
        data = [
            {
                'id': ticket.id,
                'asunto': ticket.asunto,
                'descripcion': ticket.descripcion,
                'prioridad': ticket.prioridad,
                'estado': ticket.estado,
                'usuario_id': ticket.usuario_id,
                'tecnico_id': ticket.tecnico_id,
                'fecha_creacion': ticket.fecha_creacion
            }
            for ticket in tickets
        ]

        # Retorna respuesta
        return ({'tickets': data}), 200

    except Exception as e:
        # Manejo de errores
        return ({'error': str(e)}), 500