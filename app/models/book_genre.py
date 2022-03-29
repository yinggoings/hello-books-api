from app import db

class BookGenre(db.Model):
    book_id = db.Column(db.Integer,db.ForeignKey('book.id'),primary_key=True,nullable=False)
    genre_id = db.Column(db.String,db.ForeignKey('genre.id'),primary_key=True,nullable=False)