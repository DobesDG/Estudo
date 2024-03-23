from flask import Flask, jsonify, request

app = Flask(__name__)

books = [    
    {
        "id": 1,
        "title": "O Mulato",
        "author": "Aluisio Azevedo"
    },
    {
        "id": 2,
        "title": "Para sempre vou te amar",
        "author": " Catherine Ryan Hyde"

    },
    {
        "id": 3,
        "title": "Senhor dos Anéis - A Sociedade do Anel",
        "author": "J.J.R Tolkien"
    }
]

# Consult
@app.route("/books",methods=["GET"])
def get_books():
    return jsonify(books)

# Consult by ID
@app.route("/books/<int:id>",methods=["GET"])
def get_books_id(id):
    for book in books:
        if book.get("id") == id:
            return jsonify(book)
# Edit 
@app.route("/books/<int:id>",methods=["PUT"])
def edit_book(id):
    edited_book = request.get_json()
    for idx, book in enumerate(books):
        if book.get("id") == id:
            books[idx].update(edited_book)
            return jsonify(books[idx])
        
# Create
@app.route("/books",methods=["POST"])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

# Delete
@app.route("/books/<int:id>",methods=["DELETE"])
def delete_book(id):
    for idx, book in enumerate(books):
        if book.get("id") == id:
            del books[idx]
    return jsonify(books)

app.run(port=5000,host="localhost",debug=True)

