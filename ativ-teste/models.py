from db import db


class Login(db.Model) :
   __tablename__ = 'login'


   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(40))
   user = db.Column(db.String(40))
   password = db.Column(db.String(30))


   def __repr__(self):
       return f'<User: {self.user} - Senha: {self.password}>'
  
