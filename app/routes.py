from app import db
from app.models.book import Book
from app.models.author import Author
from app.models.genre import Genre
from flask import request, Blueprint, make_response, jsonify

books_bp = Blueprint("books", __name__, url_prefix="/books")
authors_bp = Blueprint("authors", __name__, url_prefix="/authors")
genres_bp = Blueprint("genres", __name__, url_prefix="/genres")

@books_bp.route("", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append(book.to_dict())
        return jsonify(books_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} successfully created", 201)


@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return make_response("", 404)

    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    elif request.method == "PUT":
        form_data = request.get_json()

        book.title = form_data["title"]
        book.description = form_data["description"]

        db.session.commit()

        return make_response(f"Book #{book.id} successfully updated")
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book #{book.id} successfully deleted")

@books_bp.route("/<book_id>/assign_genres", methods=["PATCH"])
def assign_genres(book_id):
    book = Book.query.get(book_id)

    if book is None:
        return make_response(f"Book #{book.id} not found", 404)
    
    request_body = request.get_json()

    for id in request_body["genres"]:
        book.genres.append(Genre.query.get(id))
    db.session.commit()

    return make_response("Genres successfully added", 200)

@authors_bp.route("", methods=["POST"])
def create_author():
        request_body = request.get_json()
        new_author = Author(name=request_body["name"])

        db.session.add(new_author)
        db.session.commit()

        return make_response(f"Author #{new_author.id} successfully created", 201)


@authors_bp.route("/<author_id>/books", methods=["GET", "POST"])
def handle_author_books(author_id):

    author = Author.query.get(author_id)
    if author is None:
        return "Author not found", 404

    if request.method == "GET":
        books_response = []
        for book in author.books:
            books_response.append(
                book.to_dict()
            )
        return jsonify(books_response)
        
    elif request.method == "POST":
        request_body = request.get_json()
        requested_author = Author.query.get(id=author_id)
        new_book = Book(title=request_body["title"],
                        description=request_body["description"],
                        author=requested_author)

        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} by {new_book.author.name} successfully created", 201)

@genres_bp.route("", methods=["GET","POST"])
def handle_genres():
    if request.method == "GET":
        genres = Genre.query.all()
        genres_response = []
        for genre in genres:
            genres_response.append({
                "id": genre.id,
                "name": genre.name
                })
        return jsonify(genres_response)
    elif request.method == "POST":
        request_body = request.get_json()

        genre = Genre(name=request_body["name"])

        db.session.add(genre)
        db.session.commit()

        return jsonify(f"Genre {genre.name} was successfully created"), 201