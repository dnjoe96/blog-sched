from app import create_app, db
from app.models import User, Post


app = create_app()

# The following function in microblog.py creates a shell context that adds the database instance and models to the shell session:
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
