import pytest
from app import create_app
from app import db
from app.models.book import Book

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    
    # designates that code block should have an application context, which lets various functionality in Flask determine what the current running app is, and particularly important important when accessing the database associated with the app
    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_books(app):
    # Arrange
    ocean_book = Book(title="Ocean Book",description="watr 4evr")
    mountain_book = Book(title="Mountain Book",description="i luv 2 climb rocks")

    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.add_all([ocean_book,mountain_book])
    db.session.commit()