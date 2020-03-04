from flask import Flask, render_template
import json
import random

def create_app():
    """
    create_app is the application factory
    """
    # Create the app
    app = Flask(__name__)

    # Add a route
    @app.route('/')
    def home():
        # Load JSON file with quotes
        with app.open_resource('quotes.json') as infile:
            imported_data = json.load(infile)

        # Format into Python list
        lst = []
        q = imported_data['quotes']
        for quote in q:
            lst.append(q[quote])

        # Select a random quote
        selected_quote = random.choice(lst)

        # Pass the selected quote to the template
        return render_template('quotes.html', quote=selected_quote)

    # Return the app
    return app
