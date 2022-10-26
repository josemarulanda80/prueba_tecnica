from aplication import db
from datetime import datetime

class Image(db.Model):
    __tablename__="images"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    filename=db.Column(db.String(50))
    created=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    preserts=db.relationship('Presert',backref="images",cascade="delete,merge")

    def __init__(self,filename):
        self.filename=filename
        
    
    def __repr__(self) -> str:
        return f'filename : {self.filename}'
class Presert(db.Model):
    __tablename__="preserts"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    img=db.Column(db.Integer,db.ForeignKey('images.id',ondelete='CASCADE'))
    value=db.Column(db.Integer)
    created=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    
    def __init__(self, img,value):
        self.img=img
        self.value=value

    def __repr__(self) -> str:
        return f'Value: {self.value}'
        

