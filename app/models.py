from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager,db

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    pic = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    profiles = db.relationship('Profile', backref = 'user', lazy = 'dynamic')
    pitch = db.relationship('Pitch', backref = 'user', lazy = "dynamic")
    word = db.relationship('Words', backref = 'user', lazy = "dynamic")

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))    

    def __repr__(self):
        return f'User {self.username}'


class Category(db.Model):
    __tablename__ = 'ibyiciro'
    id = db.Column(db.Integer,primary_key = True)
    type_cate = db.Column(db.String(255))

    def ububiko(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_ibyiciro(cls):
        ibyiciro = Category.query.all()
        return ibyiciro


class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer, primary_key = True)
    head = db.Column(db.String(255))
    text = db.Column(db.String)
    ibyiciro = db.Column(db.Integer, db.ForeignKey('ibyiciro.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    word = db.relationship('Words', backref = 'pitch', lazy = "dynamic")
    vote = db.relationship('Tora', backref = 'pitch', lazy = "dynamic")

    def ububiko_pitch(self):
        db.session.add(self)
        db.session.commit()

    def get_pi(id):
        tone = Pitch.query.filter_by(category=id).all()
        return tone        


class Words(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key = True)
    texto = db.Column(db.String)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    pitch = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    vote = db.relationship('Tora', backref = 'word', lazy = "dynamic")

    def save_words(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_words(self, id):
        point = Words.query.order_by(Words.time_posted.desc()).filter_by(pitch=id).all()
        return point


class Tora(db.Model):
    __tablename__ = 'vote'
    id = db.Column(db.Integer, primary_key = True)
    count = db.Column(db.Integer)
    pitch = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    word = db.Column(db.Integer, db.ForeignKey('word.id'))

    def save_itora(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_itora(cls,user_id,pitch_id):
        amatora = Vote.query.filter_by(user=user_id, pitch=pitch_id).all()
        return amatora


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key = True)
    pic_path = db.Column(db.String())
    user = db.Column(db.Integer, db.ForeignKey("user.id"))        