import flask


from app import main


class TestMain:
    def test_main_app(self) -> None:
        assert isinstance(main.app, flask.Flask)

    def test_index_page(self) -> None:
        assert '<html>' in main.index()
        assert f'href="{main.Endpoints.NOTES}' in main.index()

    def test_routes_exist(self) -> None:
        endpoints = (
            value
            for attr, value in vars(main.Endpoints).items()
            if not attr.startswith('__') and not attr.endswith('__')
        )

        rules = main.app.url_map.iter_rules()

        for route in endpoints:
            assert route in (str(rule) for rule in rules)
