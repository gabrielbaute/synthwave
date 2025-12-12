import subprocess
import logging
import os
from rich.console import Console
from rich.table import Table
from app.services.image_utils import make_square_cover

console = Console()

def run(args):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    os.makedirs(args.output, exist_ok=True)
    console.print(f"[bold cyan]Downloading from YouTube:[/bold cyan] {args.url}")

    # Descargar audio
    cmd = [
        "yt-dlp",
        "--quiet",
        "--progress",
        "--no-warnings",
        "-x", "--audio-format", args.format,
        "-o", f"{args.output}/%(title)s.%(ext)s",
        args.url
    ]
    subprocess.run(cmd)

    console.print(f"[bold green]Download complete in {args.format.upper()} format![/bold green]")

    # Descargar miniatura
    thumb_cmd = [
        "yt-dlp",
        "--quiet",
        "--progress",
        "--no-warnings",
        "--skip-download",
        "--write-thumbnail",
        "-o", f"{args.output}/%(title)s.%(ext)s",
        args.url
    ]
    subprocess.run(thumb_cmd)

    SUPPORTED_IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

    cover_file = None
    for file in os.listdir(args.output):
        if file.lower().endswith(SUPPORTED_IMAGE_EXTENSIONS):
            cover_path = os.path.join(args.output, file)
            square_cover = os.path.join(args.output, "cover.jpeg")
            make_square_cover(cover_path, square_cover)
            cover_file = square_cover
            console.print(f"[bold magenta]Cover normalized to 1:1:[/bold magenta] {square_cover}")
            break

    # Buscar el archivo de audio descargado
    audio_file = None
    for file in os.listdir(args.output):
        if file.lower().endswith(f".{args.format}"):
            audio_file = os.path.join(args.output, file)
            break

    # Mostrar tabla resumen
    table = Table(title="Download Summary", border_style="blue")
    table.add_column("Item", style="cyan", justify="right")
    table.add_column("Value", style="green")

    if audio_file:
        size_mb = os.path.getsize(audio_file) / (1024 * 1024)
        table.add_row("Audio File", os.path.basename(audio_file))
        table.add_row("Format", args.format.upper())
        table.add_row("Size", f"{size_mb:.2f} MB")

    if cover_file:
        table.add_row("Cover", os.path.basename(cover_file))

    table.add_row("Output Dir", args.output)
    table.add_row("Source URL", args.url)

    console.print(table)
