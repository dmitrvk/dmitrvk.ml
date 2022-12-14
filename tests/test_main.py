import http
import pathlib

import flask
import pytest

from app import main


@pytest.fixture
def app() -> flask.Flask:
    yield main.app


@pytest.fixture
def client(app: flask.Flask):
    return app.test_client()


class TestMain:
    def test_main_app(self) -> None:
        assert isinstance(main.app, flask.Flask)

    def test_index_page(self, client) -> None:
        response = client.get('/').data.decode('utf-8')
        assert f'href="{main.Endpoints.NOTES}"' in response

    def test_resume_page(self, client) -> None:
        response = client.get(f'{main.Endpoints.RESUME}').data.decode('utf-8')
        assert '<img' in response

    def test_notes_page(self, client, fs) -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        notes_directory = base_directory / 'public' / 'notes'

        fs.add_real_directory(base_directory / 'app' / 'templates')
        fs.create_dir(notes_directory / 'python')
        fs.create_dir(notes_directory / 'linux')

        response = client.get('/notes').data.decode('utf-8')

        assert 'href="/notes/python"' in response
        assert 'href="/notes/linux"' in response

    def test_music_page(self, client, fs) -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        notes_directory = base_directory / 'public' / 'music'

        fs.add_real_directory(base_directory / 'app' / 'templates')
        fs.create_dir(notes_directory / 'piece')

        response = client.get(f'{main.Endpoints.MUSIC}').data.decode('utf-8')

        assert 'href="/music/piece"' in response

    def test_note_viewer_page(self, client, fs) -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        python_directory = base_directory / 'public' / 'notes' / 'python'

        fs.add_real_directory(base_directory / 'app' / 'templates')
        fs.create_file(python_directory / 'pages' / 'python-0.png')
        fs.create_file(python_directory / 'pages' / 'python-1.png')
        fs.create_file(python_directory / 'pages' / 'python-2.png')

        response = client.get('/notes/python').data.decode('utf-8')
        assert response.count('<img') == 3

    def test_note_viewer_page_not_found(self, client, fs) -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        fs.add_real_directory(base_directory / 'app' / 'templates')

        response = client.get('/notes/python')
        assert response.status_code == http.HTTPStatus.NOT_FOUND
        assert 'dmitrvk.ml' in response.data.decode('utf-8')

    def test_piece_viewer_page(self, client, fs) -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        piece_directory = base_directory / 'public' / 'music' / 'piece'

        fs.add_real_directory(base_directory / 'app' / 'templates')
        fs.create_file(piece_directory / 'piece-page1.png')
        fs.create_file(piece_directory / 'piece-page2.png')

        response = client.get('/music/piece').data.decode('utf-8')
        assert response.count('<img') == 2

    def test_piece_viewer_page_not_found(self, client, fs) -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        fs.add_real_directory(base_directory / 'app' / 'templates')

        response = client.get('/music/piece')
        assert response.status_code == http.HTTPStatus.NOT_FOUND
        assert 'dmitrvk.ml' in response.data.decode('utf-8')

    def test_routes_exist(self) -> None:
        endpoints = (
            value
            for attr, value in vars(main.Endpoints).items()
            if not attr.startswith('__') and not attr.endswith('__')
        )
        app_endpoints = [str(rule) for rule in main.app.url_map.iter_rules()]

        assert all(endpoint in app_endpoints for endpoint in endpoints)
