from flask import render_template
from app import app
from app.models import User, Post

@app.route('/')
def index():
    # Fetch all posts from the database
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    # Fetch all users from the database
    users = User.query.all()

    return render_template('about.html', users=users)
