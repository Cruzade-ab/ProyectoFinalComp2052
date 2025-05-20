from flask import Blueprint, request, jsonify
from app.models import db, Ticket
from datetime import datetime, timezone

# Blueprint solo con endpoints de prueba para tickets
main = Blueprint('main', __name__)

@main.route('/') # Ambas rutas llevan al mismo lugar
@main.route('/dashboard')
def index():
    """
    Página de inicio pública (home).
    """
    return '<h1>Corriendo en Modo de Prueba.</h1>'

@main.route('/tickets', methods=['GET'])
def listar_tickets():
    """
    Retorna una lista de tickets (JSON).
    """
    tickets = Ticket.query.all()

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
    return jsonify(data), 200


@main.route('/tickets/<int:id>', methods=['GET'])
def listar_un_ticket(id):
    """
    Retorna un solo ticket por su ID (JSON).
    """
    ticket = Ticket.query.get_or_404(id)

    data ={
        'id': ticket.id,
        'asunto': ticket.asunto,  
        'descripcion': ticket.descripcion,
        'prioridad': ticket.prioridad,
        'estado': ticket.estado, 
        'usuario_id': ticket.usuario_id,
        'tecnico_id': ticket.tecnico_id,
        'fecha_creacion': ticket.fecha_creacion  
    }

    return jsonify(data), 200


@main.route('/tickets', methods=['POST'])
def crear_ticket():
    """
    Crea un ticket sin validación.
    Espera JSON con 'titulo', 'descripcion' y 'tecnico_id'.
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    ticket = Ticket(
        asunto=data.get('asunto'),  
        descripcion=data.get('descripcion'),
        prioridad=data.get('prioridad'), 
        estado=data.get('estado'),  
        usuario_id=data.get('usuario_id'),  
        tecnico_id=data.get('tecnico_id'),  
       fecha_creacion=datetime.now(timezone.utc)
    )
    
    db.session.add(ticket)
    db.session.commit()

    return jsonify({'message': 'Ticket creado', 'id': ticket.id, 'tecnico_id': ticket.tecnico_id}), 201

@main.route('/tickets/<int:id>', methods=['PUT'])
def actualizar_ticket(id):
    """
    Actualiza un ticket sin validación de usuario o permisos.
    """
    ticket = Ticket.query.get_or_404(id)
    data = request.get_json()

    ticket.asunto = data.get('asunto', ticket.asunto)  
    ticket.descripcion = data.get('descripcion', ticket.descripcion)
    ticket.prioridad = data.get('prioridad', ticket.prioridad) 
    ticket.estado = data.get('estado', ticket.estado)  
    ticket.usuario_id = data.get('usuario_id', ticket.usuario_id)  
    ticket.tecnico_id = data.get('tecnico_id', ticket.tecnico_id)
    ticket.fecha_creacion = data.get('fecha_creacion', ticket.fecha_creacion)  

    db.session.commit()

    return jsonify({'message': 'Ticket actualizado', 'id': ticket.id}), 200

@main.route('/tickets/<int:id>', methods=['DELETE'])
def eliminar_ticket(id):
    """
    Elimina un ticket sin validación de permisos.
    """
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()

    return jsonify({'message': 'Ticket eliminado', 'id': ticket.id}), 200
