from api import db

class TagModel(db.Model):
   __tablename__ = 'tag' # эта штука меняет название таблицы, изначально оно называется как класс
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), unique=True, nullable=False) #поле уникальное и обязательное