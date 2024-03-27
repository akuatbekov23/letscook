from flask import render_template
from . import app, mongo

@app.route('/')
def index():
    # Example: Fetching groceries from MongoDB
    groceries = mongo.db.groceries.find()
    return render_template('index.html', groceries=groceries)
