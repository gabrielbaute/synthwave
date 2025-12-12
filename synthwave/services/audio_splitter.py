import os
import subprocess
import logging
from typing import List, Optional
from synthwave.schemas import TrackList, Track

class FFmpegSplitter:
    def __init__(self, input_file: str, output_dir: str = "output"):
        self.input_file = input_file
        self.output_dir = output_dir
        self.logger = logging.getLogger(self.__class__.__name__)
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _sanitize_filename(self, title: str) -> str:
        """
        Avoids problematic characters in filenames.

        Args:
            title (str): The track title.

        Returns:
            str: The sanitized track title.
        """
        return "".join(c if c.isalnum() or c in " _-" else "_" for c in title)
    
    def _ffmpeg_command(self, track: Track, output_path: str) -> List[str]:
        """
        FFMPEG Options for cmd

        Args:
            track (Track): the track info parsed
        
        Returns:
            List(str): list of options for ffmpeg with track info
        """
        cmd = ["ffmpeg", "-y", "-i", self.input_file, "-ss", str(track.start)]
        if track.end is not None:
            cmd += ["-to", str(track.end)]
        cmd += ["-c", "copy", output_path]
        return cmd

    def split_track(self, track: Track, index: int):
        """
        Split one single track

        Args:
            track (Track): Track info with times and title
            index (int): Position of track in tracklist
        """
        filename = f"{index:02d} - {self._sanitize_filename(track.title)}.mp3"
        output_path = os.path.join(self.output_dir, filename)

        cmd = self._ffmpeg_command(track, output_path)
        self.logger.debug(f"Exporting: {output_path}")
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            self.logger.error(f"FFmpeg error on {track.title}: {result.stderr}")

        return output_path

    def split_all(self, tracklist: TrackList):
        """
        Split all the file

        Args:
            tracklist (Tracklist): a Traclist object with all the tracks
        """
        outputs = []
        for i, track in enumerate(tracklist.tracks, start=1):
            out = self.split_track(track, i)
            outputs.append(out)
        self.logger.info(f"Split all tracks: {len(outputs)}")
        return outputs
