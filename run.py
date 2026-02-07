import argparse

from anime_dl import anime_dl
from anime_dl.utils.logger import Logger

logger = Logger()

def main():
    parser = argparse.ArgumentParser(description="anime-dl: download anime / animation content (authorized only)")

    # Optional flag for listing supported sites
    parser.add_argument(
        "--list-sites",
        action="store_true",
        help="Show all supported sites / extractors"
    )

    # URL is now optional if using --list-sites
    parser.add_argument(
        "url",
        nargs="?",
        help="URL of the anime / animation content to download"
    )

    args = parser.parse_args()

    try:
        if args.list_sites:
            extractors = anime_dl.list_extractors()
            print("Supported extractors:")
            for e in extractors:
                print(f"- {e}")
        elif args.url:
            anime_dl.main(args.url)
        else:
            parser.print_help()
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    main()