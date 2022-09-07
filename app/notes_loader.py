import pathlib


def get_list() -> list:
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

def get(note: str) -> dict | None:
    base_directory = pathlib.Path(__file__).resolve().parent.parent
    notes_directory = base_directory / 'public' / 'notes'

    note_directory = notes_directory / note
    pages_directory = note_directory / 'pages'

    if not pages_directory.exists():
        return None

    pages = (page for page in pages_directory.iterdir())
    pages_urls = sorted(
        f'/public/notes/{note}/pages/{page.name}' for page in pages
    )

    return {
        'name': note,
        'pages': pages_urls,
    }
