from app import db, ma

class Ejemplo(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(30),nullable = False)
    

    def __init__(self, nombre):
        self.nombre = nombre

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Ejemplo(nombre={self.nombre})"

class EjemploSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ejemplo