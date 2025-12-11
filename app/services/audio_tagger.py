import logging
from typing import List
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TRCK, APIC, TDRC, TCON
from mutagen.mp4 import MP4, MP4Cover
from app.schemas import TrackList, Track

class MutagenTagger:
    def __init__(self, album: str = "Unknown Album", artist: str = "Unknown Artist", year: int = None, genre: str = None, cover: str = None):
        self.album = album
        self.artist = artist
        self.genre = genre
        self.cover = cover
        self.year = year
        self.logger = logging.getLogger(self.__class__.__name__)

    def _add_cover_to_mp3(self, audio: ID3,  track: Track, file_path: str):
        """
        Add image cover to mp3 file

        Args:
            audio (ID3): audiofile object
            track (Track): metadata from the track object
            file_path (str): path to the audiofile
        """
        try:
            self.logger.info(f"Adding cover to: {track.title}")
            with open(self.cover, "rb") as img:
                audio.add(APIC(
                    encoding=3,
                    mime="image/jpeg",
                    type=3,  # portada frontal
                    desc="Cover",
                    data=img.read()
                )
            )
            audio.save(file_path)
        except Exception as e:
            self.logger.error(f"Error adding cover to {track.title}: {e}")

    def tag_mp3(self, file_path: str, track: Track, index: int):
        """
        Add metadata to mp3 file

        Args:
            file_path (str): path to the audiofile
            track (Track): metadata from the track object
            index (int): position of track in tracklist
        """
        audio = ID3(file_path)
        audio.add(TIT2(encoding=3, text=track.title))
        audio.add(TALB(encoding=3, text=self.album))
        audio.add(TPE1(encoding=3, text=self.artist))
        audio.add(TRCK(encoding=3, text=str(index)))
        
        if self.year:
            audio.add(TDRC(encoding=3, text=str(self.year)))
        
        if self.genre:
            audio.add(TCON(encoding=3, text=self.genre))
        audio.save()

        # Portada con ID3
        if self.cover:
            self._add_cover_to_mp3(audio, track, file_path)

        self.logger.info(f"Tagged MP3: {file_path}")

    def tag_m4a(self, file_path: str, track: Track, index: int):
        """
        Add metadata to m4a file

        Args:
            file_path (str): path to the audiofile
            track (Track): metadata from the track object
            index (int): position of track in tracklist
        """
        audio = MP4(file_path)
        audio["\xa9nam"] = track.title
        audio["\xa9alb"] = self.album
        audio["\xa9ART"] = self.artist
        audio["trkn"] = [(index, 0)]
        if self.genre:
            audio["\xa9gen"] = self.genre
        
        if self.year:
            audio["\xa9day"] = str(self.year)

        # Añadir portada si existe
        if self.cover:
            with open(self.cover, "rb") as img:
                audio["covr"] = [MP4Cover(img.read(), imageformat=MP4Cover.FORMAT_JPEG)]

        audio.save()
        self.logger.info(f"Tagged M4A: {file_path}")

    def tag_all(self, files: List[str], tracklist: TrackList):
        """
        Tag all files in the output directory

        Args:
            files (List): List of filepaths
            tracklist (Tracklist): Tracklist object with all tracks
        """
        for i, (file_path, track) in enumerate(zip(files, tracklist.tracks), start=1):
            if file_path.endswith(".mp3"):
                self.tag_mp3(file_path, track, i)
            elif file_path.endswith(".m4a"):
                self.tag_m4a(file_path, track, i)
