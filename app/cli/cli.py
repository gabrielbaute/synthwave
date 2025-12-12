from app.cli.parser import generate_parser
from app.cli.commands import split, version

def main():
    parser = generate_parser()
    args = parser.parse_args()

    if args.command == "split":
        split.run(args)
    elif args.command == "version":
        version.run()

if __name__ == "__main__":
    main()
