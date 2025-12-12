from app.cli.parser import generate_parser
from app.cli.commands import split, version, download, clean

def main():
    parser = generate_parser()
    args = parser.parse_args()

    if args.command == "split":
        split.run(args)
    elif args.command == "download":
        download.run(args)
    elif args.command == "clean":
        clean.run(args)
    elif args.command == "version":
        version.run()

if __name__ == "__main__":
    main()
