from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    bio = db.Column(db.String(250))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)

# Function to create the database with sample data (!you can remove it )
def create_sample_data():
    # Create some users
    user1 = User(username='Tyler Enos', email='tyler@example.com', bio='Programmer, Designer, Developer')
    user2 = User(username='John Doe', email='john@example.com', bio='Software Engineer')
    user3 = User(username='Jane Smith', email='jane@example.com', bio='Web Developer')

    # Set passwords for the users
    user1.set_password('password1')
    user2.set_password('password2')
    user3.set_password('password3')

    # Create some posts
    post1 = Post(title='First Post', content='This is my first blog post!', author=user1)
    post2 = Post(title='Second Post', content='Another great blog post!', author=user2)
    post3 = Post(title='Hello World', content='My first blog post ever!', author=user3)

    # Add the objects to the session
    db.session.add_all([user1, user2, user3, post1, post2, post3])
    db.session.commit()

# Create the database tables if they don't exist
db.create_all()

# Check if the User table is empty
if not User.query.first():
    create_sample_data()
