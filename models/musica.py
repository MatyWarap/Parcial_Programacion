from models.db import db

class Musica(db.Model):
    __tablename__ = 'musica'

    id = db.Column(db.Integer, primary_key=True)
    cancion = db.Column(db.String(100))
    artista = db.Column(db.String(100))
    album = db.Column(db.String(100))
    anio = db.Column(db.Integer)
    duracion = db.Column(db.Integer) # Duracion de la cancion en segundos
    fecha_lanzamiento = db.Column(db.Date)
    hora_estreno = db.Column(db.Time)
    descripcion = db.Column(db.Text)
    email_contacto = db.Column(db.String(100))
    activo = db.Column(db.Boolean, default=True)

    def __init__(self, cancion, artista, album, anio, duracion, fecha_lanzamiento, hora_estreno, descripcion, email_contacto, activo=True):
        self.cancion = cancion
        self.artista = artista
        self.album = album
        self.anio = anio
        self.duracion = duracion
        self.fecha_lanzamiento = fecha_lanzamiento
        self.hora_estreno = hora_estreno
        self.descripcion = descripcion
        self.email_contacto = email_contacto
        self.activo = activo

    def serialize(self):
        return {
            'id': self.id,
            'cancion': self.cancion,
            'artista': self.artista,
            'album': self.album,
            'anio': self.anio,
            'duracion': self.duracion,
            'fecha_lanzamiento': self.fecha_lanzamiento,
            'hora_estreno': self.hora_estreno.strftime("%H:%M:%S") if self.hora_estreno else None, # Formatea la hora para poder devolverla en formato JSON
            'descripcion': self.descripcion,
            'email_contacto': self.email_contacto,
            'activo': self.activo
        }