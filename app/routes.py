from flask import Blueprint, jsonify, abort

class Book:
    def __init__(self,id,title,description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1,"The Watchmen","comic"),
    Book(2,"The New York Times","newspaper"),
    Book(3,"Harry Potter","fiction")
    ]

books_bp = Blueprint("books_bp",__name__,url_prefix="/books")

@books_bp.route("",methods=["GET"])
def books_info():
    books_response = []
    for book in books:
        books_response.append(
            {"id":book.id,
            "title":book.title,
            "description":book.description}
        )
    return jsonify(books_response)

@books_bp.route("/<book_id>",methods=["GET"])
def book_info(book_id):
    if book_id.isdigit():
        book_id = int(book_id)
        for book in books:
            if book.id == book_id:
                return {
                    "id":book.id,
                    "title":book.title,
                    "description":book.description
                }
    abort(404)