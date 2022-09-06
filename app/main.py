from typing import Final

import flask
import whitenoise


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


@app.route(Endpoints.ROOT)
def index():
    return flask.render_template('index.html')


@app.route(Endpoints.NOTES)
def notes():
    return '<html></html>'
