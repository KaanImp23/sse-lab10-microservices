from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

URL = "http://book-api-server.chfaavdwc8g9bqd6.uksouth.azurecontainer.io:5000/books"

@app.route('/books')
def get_books():
    # Make a request to the first service to get all books
    response = requests.get(URL)
    books = response.json()
    
    # Extract genre parameter from the request URL
    genre = request.args.get('genre')

    # Filter books by genre if provided
    if genre:
        filtered_books = [book for book in books if genre.lower() in book.get('genre', '').lower()]
        return jsonify(filtered_books)
    else:
        return jsonify(books)
