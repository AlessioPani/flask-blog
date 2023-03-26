from blog import app
from blog.models import Post
from flask import render_template


@app.route("/")
def homepage():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    
    return render_template("homepage.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")
