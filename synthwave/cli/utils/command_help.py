from rich.console import Console
from rich.table import Table

console = Console()

def print_command_help(command: str):
    table = Table(
        title=f"[bold magenta]Help for '{command}'[/bold magenta]",
        border_style="blue",
        padding=(0, 2),
    )
    table.add_column("Flag / Argument", style="cyan", justify="right")
    table.add_column("Description", style="green")

    if command == "split":
        options = {
            "tracklist": "Path to tracklist .txt file",
            "audio": "Path to full audio file (mp3/m4a)",
            "--output": "Output directory for tracks (default: output)",
            "--album": "Album name (default: Unknown Album)",
            "--artist": "Artist name (default: Unknown Artist)",
            "--year": "Year of release",
            "--genre": "Genre of the album",
            "--cover": "Path to cover image (jpg/png)",
        }
    elif command == "download":
        options = {
            "url": "YouTube video URL",
            "--output": "Output directory (default: downloads)",
            "--format": "Audio format to export (mp3 or m4a, default: mp3)",
        }
    elif command == "clean":
        options = {
            "--output": "Target directory to clean (default: downloads)",
            "--all": "Remove entire directory contents",
        }
    elif command == "check":
        options = {}
    elif command == "version":
        options = {}

    for opt, desc in options.items():
        table.add_row(opt, desc)

    console.print(table)
