from app import db
from flask.ext.login import UserMixin
from hashlib import md5

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mobile=db.Column(db.Integer,unique=True)
    password=db.Column(db.String(50))
    otp=db.Column(db.Integer)
    temp=db.Column(db.Integer)
    
    def avatar(self, size):
       return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)
   

    def __init__(self ,email ,name,password):
        #self.id = id
        self.name=name
        self.password = password
        self.email = email
        #self.social_id = social_id    
	
   
class Places(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    place = db.Column(db.String(64), index=True, unique=True)
   
   
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)


