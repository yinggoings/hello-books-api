import json

def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# 1
def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()
    # returning NoneType
    
    #Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1, 
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

# 2
def test_get_one_book_with_no_records(client):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

# 3
def test_get_all_books(client, two_saved_books):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{"id":1,"title":"Ocean Book","description":"watr 4evr"},{"id":2,"title":"Mountain Book","description":"i luv 2 climb rocks"}]

# 4
def test_post_book(client):
    # Arrange
    book_data = {
        "title": "Ocean Book",
        "description": "watr 4evr"}
    # headers = {'Content-Type': 'application/json'}

    # Act
    post_response = client.post("/books",data=json.dumps(book_data),content_type="application/json")
    get_response = client.get("/books/1")
    response_body = get_response.get_json()

    # Assert
    assert post_response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }