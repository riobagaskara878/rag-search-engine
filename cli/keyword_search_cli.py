import argparse
from lib.search_utils import loader
from lib.keyword_search import search_movies

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            data = loader("data/movies.json")
            results = search_movies(data["movies"], args.query)
            for number, movie in enumerate(results, start=1):
                print(f"{number}. {movie["title"]}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()