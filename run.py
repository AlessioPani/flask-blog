from blog import app, db
from blog.models import Post, User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
