from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    bio = db.Column(db.String(250))
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Post {self.title}>"


def load_user(user_id):
    return User.query.get(int(user_id))


def create_sample_data():
    """Create sample users & posts only if database is empty"""
    if User.query.first():
        return  # Skip if users exist

    users = [
        User(username="0xJaneDoe.eth", email="jane@example.com", bio="Web3 Developer"),
        User(
            username="cryptosmith.lens",
            email="crypto@example.com",
            bio="Blockchain Engineer",
        ),
        User(
            username="metaverse.alice", email="alice@example.com", bio="Digital Artist"
        ),
    ]

    for user in users:
        user.set_password("password123")

    posts = [
        Post(
            title="The Future of Web3 Development",
            content="Explore the revolutionary world of decentralized applications and how they're reshaping the digital landscape...",
            author=users[0],
            timestamp=datetime(2024, 3, 15),
            image="https://images.unsplash.com/photo-1639762681485-074b7f938ba0?auto=format&fit=crop&q=80&w=800",
        ),
        Post(
            title="Understanding DeFi Protocols",
            content="Dive deep into decentralized finance protocols and discover how they're transforming traditional banking...",
            author=users[1],
            image="https://images.unsplash.com/photo-1639762681485-074b7f938ba0?auto=format&fit=crop&q=80&w=800",
        ),
        Post(
            title="NFT Revolution in Digital Art",
            content="Explore how NFTs are revolutionizing digital ownership and creating new opportunities for artists...",
            author=users[2],
            image="https://images.unsplash.com/photo-1639762681485-074b7f938ba0?auto=format&fit=crop&q=80&w=800",
        ),
    ]

    db.session.add_all(users + posts)
    db.session.commit()
