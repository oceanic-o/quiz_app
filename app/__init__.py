from flask import Flask
from jinja2 import Environment

app = Flask(__name__)
app.config.from_object('config')

@app.context_processor
def utility_processor():
    def enumerate_func(iterable, start=0):
        return enumerate(iterable, start)
    return dict(enumerate=enumerate_func)

from app import routes
