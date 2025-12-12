import logging
from rich.console import Console
from rich.table import Table
from synthwave.services import TrackListParser, FFmpegSplitter, MutagenTagger

console = Console()

def run(args):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # 1. Parsear tracklist
    parser_service = TrackListParser(args.tracklist)
    tracklist = parser_service.parse()
    console.print(f"[bold green]Tracklist loaded:[/bold green] {tracklist.total_tracks} tracks")

    # 2. Split audio
    splitter = FFmpegSplitter(args.audio, args.output)
    files = splitter.split_all(tracklist)
    console.print(f"[bold cyan]Audio split complete:[/bold cyan] {len(files)} files generated")

    # 3. Tagging
    tagger = MutagenTagger(
        album=args.album,
        artist=args.artist,
        year=args.year,
        genre=args.genre,
        cover=args.cover
    )
    tagger.tag_all(files, tracklist)
    console.print("[bold magenta]Tagging complete![/bold magenta]")

    # 4. Tabla resumen
    table = Table(title="Generated Tracks")
    table.add_column("Index", justify="right")
    table.add_column("Title", style="cyan")
    table.add_column("File", style="green")

    for i, (file_path, track) in enumerate(zip(files, tracklist.tracks), start=1):
        table.add_row(str(i), track.title, file_path)

    console.print(table)
