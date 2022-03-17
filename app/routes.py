from app import db
from app.models.book import Book
from app.models.author import Author
from flask import Blueprint, jsonify, make_response, request, abort

books_bp = Blueprint("books",__name__,url_prefix="/books")
authors_bp = Blueprint("authors",__name__,url_prefix="/authors")

@books_bp.route("",methods=["GET","POST"])
def handle_books():
    if request.method=="POST":
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])
        db.session.add(new_book)
        db.session.commit()
        return make_response(f"Book {new_book.title} successfully created", 201)
    elif request.method=="GET":
        title_query = request.args.get("title")
        if title_query:
            books = Book.query.filter_by(title=title_query)
        else:
            books = Book.query.all()
        # books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id":book.id,
                "title":book.title,
                "description":book.description
            })
        return jsonify(books_response)
        
@books_bp.route("/<book_id>",methods=["GET","PUT","DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return make_response(f"Book #{book_id} is invalid",404)
    if request.method=="GET":
        return {
            "id":book.id,
            "title":book.title,
            "description":book.description
        }
    elif request.method=="PUT":
        form_data = request.get_json()
        book.title = form_data["title"]
        book.description = form_data["description"]
        db.session.commit()
        return make_response(f"Book #{book.id} successfully updated", 201)
    elif request.method=="DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book #{book.id} successfully deleted", 201)

@authors_bp.route("",methods=["GET","POST"])
def author_info():
    if request.method == "GET":
        authors = Author.query.all()
        authors_response = []
        for author in authors:
            authors_response.append({
                "id":author.id,
                "name":author.name
            })
        return jsonify(authors_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_author = Author(name=request_body["name"])
        db.session.add(new_author)
        db.session.commit()
        return make_response(f"Autor {new_author.name} successfully created", 201)






# from flask import Blueprint, jsonify, abort

# class Book:
#     def __init__(self,id,title,description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1,"The Watchmen","comic"),
#     Book(2,"The New York Times","newspaper"),
#     Book(3,"Harry Potter","fiction")
#     ]

# books_bp = Blueprint("books_bp",__name__,url_prefix="/books")

# @books_bp.route("",methods=["GET"])
# def books_info():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {"id":book.id,
#             "title":book.title,
#             "description":book.description}
#         )
#     return jsonify(books_response)

# @books_bp.route("/<book_id>",methods=["GET"])
# def book_info(book_id):
#     if book_id.isdigit():
#         book_id = int(book_id)
#         for book in books:
#             if book.id == book_id:
#                 return {
#                     "id":book.id,
#                     "title":book.title,
#                     "description":book.description
#                 }
#     abort(404)