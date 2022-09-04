from typing import Final

import flask


app = flask.Flask(__name__)


class Endpoints:
    ROOT: Final[str] = '/'
    NOTES: Final[str] = '/notes'


@app.route(Endpoints.ROOT)
def index():
    return flask.render_template('index.html')


@app.route(Endpoints.NOTES)
def notes():
    return '<html></html>'
