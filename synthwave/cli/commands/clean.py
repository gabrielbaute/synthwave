import os
import shutil
from rich.console import Console

console = Console()

def run(args):
    if not os.path.exists(args.output):
        console.print(f"[red]Directory not found:[/red] {args.output}")
        return

    if args.all:
        shutil.rmtree(args.output)
        os.makedirs(args.output, exist_ok=True)
        console.print(f"[bold red]Cleaned entire directory:[/bold red] {args.output}")
    else:
        for file in os.listdir(args.output):
            if file.endswith((".webp", ".jpg", ".png", ".jpeg", ".webm")):
                os.remove(os.path.join(args.output, file))
        console.print(f"[bold yellow]Removed thumbnails and temp files from:[/bold yellow] {args.output}")
