import http
from typing import Final

import flask
import whitenoise

from app import music_loader, notes_loader

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
    RESUME: Final[str] = '/resume'
    MUSIC: Final[str] = '/music'
    NOTES: Final[str] = '/notes'
    NOTE_VIEWER: Final[str] = '/notes/<note>'
    PIECE_VIEWER: Final[str] = '/music/<piece>'


@app.route(Endpoints.ROOT)
def index():
    return flask.render_template('index.html')


@app.route(Endpoints.RESUME)
def resume():
    return flask.render_template('resume.html')


@app.route(Endpoints.NOTES)
def notes():
    return flask.render_template('notes.html', notes=notes_loader.get_list())


@app.route(Endpoints.MUSIC)
def music():
    return flask.render_template('music.html', music=music_loader.get_list())


@app.route(Endpoints.NOTE_VIEWER)
def note_viewer(note: str):
    _note = notes_loader.get(note)

    if not _note:
        flask.abort(http.HTTPStatus.NOT_FOUND)

    return flask.render_template(
        'note_viewer.html',
        note=_note,
    )


@app.route(Endpoints.PIECE_VIEWER)
def piece_viewer(piece: str):
    _piece = music_loader.get(piece)

    if not _piece:
        flask.abort(http.HTTPStatus.NOT_FOUND)

    return flask.render_template(
        'piece_viewer.html',
        piece=_piece
    )


@app.errorhandler(http.HTTPStatus.NOT_FOUND)
def page_not_found(_):
    return flask.render_template('404.html'), http.HTTPStatus.NOT_FOUND


@app.errorhandler(http.HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_server_error(_):
    return (
        flask.render_template('500.html'),
        http.HTTPStatus.INTERNAL_SERVER_ERROR,
    )
