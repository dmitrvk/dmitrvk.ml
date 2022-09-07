import http
from typing import Final

import flask
import whitenoise

from app import notes_loader


app = flask.Flask(__name__)

app.wsgi_app = whitenoise.WhiteNoise(
    application=app.wsgi_app,
    root='static/',
    prefix='static/',
)

app.wsgi_app.add_files(
    root='public/',
    prefix='public/',
)


class Endpoints:
    ROOT: Final[str] = '/'
    NOTES: Final[str] = '/notes'
    NOTE_VIEWER: Final[str] = '/notes/<note>'


@app.route(Endpoints.ROOT)
def index():
    return flask.render_template('index.html')


@app.route(Endpoints.NOTES)
def notes():
    return flask.render_template('notes.html', notes=notes_loader.get_list())


@app.route(Endpoints.NOTE_VIEWER)
def note_viewer(note: str):
    note = notes_loader.get(note)

    if not note:
        flask.abort(http.HTTPStatus.NOT_FOUND)

    return flask.render_template(
        'note_viewer.html',
        note=note,
    )
