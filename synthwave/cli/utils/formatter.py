from rich.console import Console
from rich.table import Table

console = Console()

def print_help():
    table = Table(
        title="[bold magenta]Synthwave CLI Help[/bold magenta]",
        border_style="blue",
        padding=(0, 2),
    )
    table.add_column("Command", style="cyan", justify="right")
    table.add_column("Description", style="green")

    commands = {
        "split": "Split audio files by tracklist and tag them with metadata",
        "download": "Download audio from YouTube",
        "clean": "Clean download directory",
        "check": "Check dependencies required for the CLI",
        "version": "Show version information",
    }

    for cmd, desc in commands.items():
        table.add_row(cmd, desc)

    console.print(table)

    console.print("\n[bold yellow]Usage examples:[/bold yellow]")
    console.print("  synth split tracklist.txt audio.mp3 --output tracks --album 'My Album'")
    console.print("  synth download https://youtu.be/XXXX --format mp3 --output downloads")
    console.print("  synth clean --output downloads --all")
    console.print("  synth check")
    console.print("  synth version")
