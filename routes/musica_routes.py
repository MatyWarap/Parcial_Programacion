from flask import Blueprint, jsonify
from models.musica import Musica
from models.db import db

cancion = Blueprint('musica', __name__, url_prefix='/api/spotify')

@cancion.route('/canciones')
def get_canciones_activas():
    canciones = Musica.query.filter_by(activo=True).all() # Filtra las canciones que estan activas

    if not canciones:
        return jsonify({'message': 'No hay canciones para mostrar'})

    return jsonify([cancion.serialize() for cancion in canciones])

@cancion.route('/canciones/<int:id>', methods=['DELETE'])
def delete_canciones(id):
    cancion = Musica.query.get(id)
    
    if not cancion: 
        return jsonify({'message': 'Cancion no encontrada'}), 404 

    cancion.activo = False
    db.session.commit()

    return jsonify({'message': f'Canción con id {id} dada de baja'}), 200

@cancion.route('/canciones/clasificadas', methods=['GET'])
def get_canciones_clasificadas():
    canciones = Musica.query.filter_by(activo=True).all() # Filtra las canciones que estan activas

    cortas = [] # Menos de 180 segundos
    medias = [] # Entre 180 y 240 segundos
    largas = [] # Mas de 340 segundos

    for cancion in canciones:
        if cancion.duracion < 180:
            cortas.append(cancion.serialize())
        elif 180 <= cancion.duracion <= 240:
            medias.append(cancion.serialize())
        elif cancion.duracion > 340:
            largas.append(cancion.serialize())

    resultado = {
        'corta': cortas,
        'media': medias,
        'larga': largas
    }

    return jsonify(resultado)