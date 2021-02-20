# '''Defines the model for our database'''
#
# from datetime import datetime
# from server import db
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     sensor = db.Column(db.String(20), unique=True, nullable=False)
#     type = db.Column(db.String(20), unique=True, nullable=False)
#     datime = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)
#
#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"