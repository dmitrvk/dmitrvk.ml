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

    def test_routes_exist(self) -> None:
        endpoints = (
            value
            for attr, value in vars(main.Endpoints).items()
            if not attr.startswith('__') and not attr.endswith('__')
        )
        app_endpoints = [str(rule) for rule in main.app.url_map.iter_rules()]

        assert all(endpoint in app_endpoints for endpoint in endpoints)
