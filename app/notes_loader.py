import pathlib


def get() -> list:
    base_directory = pathlib.Path(__file__).resolve().parent.parent
    notes_directory = base_directory / 'public' / 'notes'

    paths = (item for item in notes_directory.iterdir() if item.is_dir())

    return [
        {
            'name': path.name,
            'url': f'/notes/{path.name}',
            'thumbnail_url':
                f'/public/notes/{path.name}/{path.name}-thumbnail.png',
        }
        for path in paths
    ]
