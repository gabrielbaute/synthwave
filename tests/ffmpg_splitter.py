import logging
from synthwave.services import TrackListParser, FFmpegSplitter


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

track_list_file = "tracklist.txt"
audio_file = "1990_Stellar_Circuit_Fleet.mp3"

parser = TrackListParser(track_list_file)
tracklist = parser.parse()

splitter = FFmpegSplitter(audio_file)
splitter.split_all(tracklist)
