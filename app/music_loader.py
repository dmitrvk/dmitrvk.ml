import pathlib


def get_list() -> list:
    base_directory = pathlib.Path(__file__).resolve().parent.parent
    music_directory = base_directory / 'public' / 'music'

    paths = (item for item in music_directory.iterdir() if item.is_dir())

    return [
        {
            'name': path.name,
            'url': f'/music/{path.name}',
            'thumbnail_url':
                f'/public/music/{path.name}/{path.name}-thumbnail.png',
        }
        for path in paths
    ]


def get(piece: str) -> dict | None:
    base_directory = pathlib.Path(__file__).resolve().parent.parent
    music_directory = base_directory / 'public' / 'music'

    piece_directory = music_directory / piece

    if not piece_directory.exists():
        return None

    pages = (
        page
        for page in piece_directory.iterdir()
        if 'page' in page.name or page.name == f'{piece}.png'
    )

    pages_urls = sorted(
        f'/public/music/{piece}/{page.name}' for page in pages
    )

    return {
        'pages': pages_urls,
    }
