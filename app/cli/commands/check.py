import shutil
import sys
from rich.console import Console
from rich.table import Table

console = Console()

DEPENDENCIES = {
    "ffmpeg": "Required for audio conversion and splitting",
    "yt-dlp": "Required for downloading from YouTube",
}

def run():
    table = Table(
        title="[bold magenta]Dependency Check[/bold magenta]",
        border_style="blue",
        padding=(0, 2),
    )
    table.add_column("Dependency", style="cyan", justify="right")
    table.add_column("Status", style="green")
    table.add_column("Description", style="yellow")

    all_ok = True
    for dep, desc in DEPENDENCIES.items():
        if shutil.which(dep):
            status = "[bold green]✓ Installed[/bold green]"
        else:
            status = "[bold red]✗ Missing[/bold red]"
            all_ok = False
        table.add_row(dep, status, desc)

    console.print(table)

    # Código de salida: 0 si todo está OK, 1 si falta algo
    if not all_ok:
        console.print("[red]Some dependencies are missing. Please install them before continuing.[/red]")
        sys.exit(1)
    else:
        console.print("[bold green]All dependencies are satisfied![/bold green]")
        sys.exit(0)
