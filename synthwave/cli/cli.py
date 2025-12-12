import sys
from synthwave.cli.parser import generate_parser
from synthwave.cli.utils import print_help, print_command_help
from synthwave.cli.commands import split, version, download, clean, check

def main():
    parser = generate_parser()
    
    if "--help" in sys.argv or "-h" in sys.argv:
        if len(sys.argv) > 1 and sys.argv[1] in ["split", "download", "clean", "check", "version"]:
            print_command_help(sys.argv[1])
        else:
            print_help()
        return
    
    if not sys.argv[1:]:
        print_help()
        return

    args = parser.parse_args()

    if args.command == "split":
        split.run(args)
    elif args.command == "download":
        download.run(args)
    elif args.command == "clean":
        clean.run(args)
    elif args.command == "check":
        check.run()
    elif args.command == "version":
        version.run()

if __name__ == "__main__":
    main()
