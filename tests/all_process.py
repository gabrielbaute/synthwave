import logging
from synthwave.services import TrackListParser, FFmpegSplitter, MutagenTagger


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

track_list_file = "tracklist.txt"
audio_file = "1990_Stellar_Circuit_Fleet.mp3"

parser = TrackListParser(track_list_file)
tracklist = parser.parse()

splitter = FFmpegSplitter(audio_file)
files = splitter.split_all(tracklist)

tagger = MutagenTagger(
    album="1990 Stellar Circuit Fleet",
    artist="Zyykron Sound",
    year=2025,
    genre="Synthwave",
    cover="cover.jpeg"
)
tagger.tag_all(files, tracklist)