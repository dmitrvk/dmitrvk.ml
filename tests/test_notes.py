import pathlib
from typing import TYPE_CHECKING

from app import notes_loader

if TYPE_CHECKING:
    from pyfakefs import fake_filesystem as fake_fs


class TestNotes:
    def test_notes_list(self, fs: 'fake_fs.FakeFilesystem') -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        notes_directory = base_directory / 'public' / 'notes'

        fs.create_dir(notes_directory / 'python')
        fs.create_dir(notes_directory / 'linux')

        notes = notes_loader.get()

        assert len(notes) == 2
        assert notes[0].get('name') == 'python'
        assert notes[0].get('url') == '/notes/python'
        assert notes[0].get('thumbnail_url') == (
            '/public/notes/python/python-thumbnail.png'
        )
