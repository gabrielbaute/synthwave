import argparse

def generate_parser():
    parser = argparse.ArgumentParser(
        description="Split audio files by tracklist and tag them with metadata",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="Commands to run")

    # -------------------------------------------
    # Subcomando: split
    # -------------------------------------------
    split_parser = subparsers.add_parser(
        "split",
        help="Split audio files by tracklist and tag them with metadata"
    )
    split_parser.add_argument("tracklist", help="Path to tracklist .txt file")
    split_parser.add_argument("audio", help="Path to full audio file (mp3/m4a)")
    split_parser.add_argument("--output", default="output", help="Output directory for tracks")
    split_parser.add_argument("--album", default="Unknown Album", help="Album name")
    split_parser.add_argument("--artist", default="Unknown Artist", help="Artist name")
    split_parser.add_argument("--year", type=int, help="Year of release")
    split_parser.add_argument("--genre", help="Genre of the album")
    split_parser.add_argument("--cover", help="Path to cover image (jpg/png)")

    # -------------------------------------------
    # Subcomando: version
    # -------------------------------------------
    subparsers.add_parser("version", help="Show version information")

    return parser
