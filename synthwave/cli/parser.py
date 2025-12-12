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
    # Subcomando: download
    # -------------------------------------------
    download_parser = subparsers.add_parser("download", help="Download audio from YouTube")
    download_parser.add_argument("url", help="YouTube video URL")
    download_parser.add_argument("--output", default="downloads", help="Output directory")
    download_parser.add_argument(
        "--format",
        choices=["mp3", "m4a"],
        default="mp3",
        help="Audio format to export (mp3 or m4a)"
    )

    # -------------------------------------------
    # Subcomando: clean
    # -------------------------------------------
    clean_parser = subparsers.add_parser("clean", help="Clean download directory")
    clean_parser.add_argument("--output", default="downloads", help="Target directory to clean")
    clean_parser.add_argument("--all", action="store_true", help="Remove entire directory contents")


    # -------------------------------------------
    # Subcomando: check
    # -------------------------------------------
    subparsers.add_parser("check", help="Check dependencies requiered for the CLI")

    # -------------------------------------------
    # Subcomando: version
    # -------------------------------------------
    subparsers.add_parser("version", help="Show version information")

    return parser
