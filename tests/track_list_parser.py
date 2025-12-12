import logging
from synthwave.services import TrackListParser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file = "tracklist.txt"
parser = TrackListParser(file)
tracklist = parser.parse()

print(f"Total time: {tracklist.total_time}")
print(f"Total tracks: {tracklist.total_tracks}")

for track in tracklist.tracks:
    print(f"Start: {track.start}, End: {track.end}, Title: {track.title}")