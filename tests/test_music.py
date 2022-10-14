import pathlib
from typing import TYPE_CHECKING

from app import music_loader

if TYPE_CHECKING:
    from pyfakefs import fake_filesystem as fake_fs


class TestMusic:
    def test_music_list(self, fs: 'fake_fs.FakeFilesystem') -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        music_directory = base_directory / 'public' / 'music'

        fs.create_dir(music_directory / 'piece')
        fs.create_dir(music_directory / 'test')

        music = music_loader.get_list()

        assert len(music) == 2
        assert music[0].get('name') == 'piece'
        assert music[0].get('url') == '/music/piece'
        assert music[0].get('thumbnail_url') == (
            '/public/music/piece/piece-thumbnail.png'
        )

    def test_piece(self, fs: 'fake_fs.FakeFilesystem') -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        piece_directory = base_directory / 'public' / 'music' / 'piece'

        fs.create_file(piece_directory / 'piece-page1.png')
        fs.create_file(piece_directory / 'piece-page2.png')

        piece = music_loader.get('piece')

        assert piece.get('pages') == [
            '/public/music/piece/piece-page1.png',
            '/public/music/piece/piece-page2.png',
        ]

    def test_piece_single_page(self, fs: 'fake_fs.FakeFilesystem') -> None:
        base_directory = pathlib.Path(__file__).resolve().parent.parent
        piece_directory = base_directory / 'public' / 'music' / 'piece'

        fs.create_file(piece_directory / 'piece.png')

        piece = music_loader.get('piece')

        assert piece.get('pages') == [
            '/public/music/piece/piece.png',
        ]

    def test_non_existing_piece(self, fs: 'fake_fs.FakeFilesystem') -> None:
        assert not music_loader.get('piece')
