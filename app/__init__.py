from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    # Import models here
    from app.models.book import Book
    from app.models.author import Author
    from app.models.genre import Genre
    from app.models.book_genre import BookGenre

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import books_bp, authors_bp, genres_bp
    app.register_blueprint(books_bp)
    app.register_blueprint(authors_bp)
    app.register_blueprint(genres_bp)

    return app
