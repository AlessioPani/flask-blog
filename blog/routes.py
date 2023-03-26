from blog import app
from flask import render_template


@app.route("/")
def homepage():
    posts = [
        {'title': 'First post', 'body': 'First body'},
        {'title': 'Second post', 'body': 'Second body'},
    ]
    some_boolean_flag = False

    return render_template("homepage.html",
                           posts=posts, boolean_flag=some_boolean_flag)


@app.route("/about")
def about():
    return render_template("about.html")
