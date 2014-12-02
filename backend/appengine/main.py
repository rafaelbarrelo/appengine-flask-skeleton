from flask import Flask, abort

app = Flask(__name__)
app.config['DEBUG'] = True



@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.route('/')
def index():
    return 'Hello Flask! =)'

