from typing import Final

import flask


app = flask.Flask(__name__)


class Endpoints:
    ROOT: Final[str] = '/'
    NOTES: Final[str] = '/notes'


@app.route(Endpoints.ROOT)
def index():
    return f'<html><a href="{Endpoints.NOTES}">Notes</a></html>'


@app.route(Endpoints.NOTES)
def notes():
    return '<html></html>'
