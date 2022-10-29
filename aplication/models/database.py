from enum import unique
from aplication import db
from datetime import datetime


class Presert(db.Model):
    __tablename__="preserts"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    filename=db.Column(db.String(50))
    value=db.Column(db.Float,unique=True)
    created=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    
    def __init__(self, filename,value):
        self.filename=filename
        self.value=value

    def __repr__(self) -> str:
        return f'Value: {self.value}'
        

