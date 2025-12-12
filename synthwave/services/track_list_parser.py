import re
import logging
from typing import List, Optional
from synthwave.schemas import Track, TrackList

class TrackListParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.time_pattern = re.compile(r"(\d{1,2}):(\d{2})(?:\s*[-–]?\s*)(.+)")
        self.logger = logging.getLogger(self.__class__.__name__)

    def load_file(self) -> List[str]:
        """
        Loads the file and returns a list of lines.

        Returns:
            List[str]: List of lines.
        """
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.logger.info(f"Loading file: {self.file_path}")
            return [line.strip() for line in f if line.strip()]
        
    def parse_track(self, line: str) -> Optional[Track]:
        """
        Parses a line and returns a Track object.

        Returns:
            Track: Track object.
            None: If the line is invalid.
        """
        match = self.time_pattern.match(line)
        if match:
            minutes, seconds, title = match.groups()
            start = int(minutes) * 60 + int(seconds)
            return Track(start=start, end=None, title=title.strip())
        else:
            self.logger.warning(f"Invalid line format: {line}")
            return None

    def parse(self) -> TrackList:
        """
        Parse the file and returns a TrackList object.

        Returns:
            TrackList: TrackList object.
        """
        lines = self.load_file()
        parsed_tracks = [self.parse_track(line) for line in lines]
        parsed_tracks = [t for t in parsed_tracks if t is not None]

        # calcular end
        for i in range(len(parsed_tracks)):
            if i + 1 < len(parsed_tracks):
                parsed_tracks[i].end = parsed_tracks[i+1].start

        return TrackList(
            tracks=parsed_tracks,
            total_time=parsed_tracks[-1].end,  # puede ser None
            total_tracks=len(parsed_tracks)
        )
