from app import db

class Missao(db.Model):
    __table__ = "missao"
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)