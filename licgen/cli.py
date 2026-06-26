import argparse
from pathlib import Path

from .core import TEMPLATES_DIR, create_license_file


def main() -> None:
    parser = argparse.ArgumentParser(description="licgen — fast and simple LICENSE file generator.")

    parser.add_argument("-l", "--list", action="store_true", help="show all available license types")

    parser.add_argument("license_type", type=str, nargs="?", help="type of license to generate")
    parser.add_argument("-a", "--author", type=str, required=False, help="name of the author")
    parser.add_argument("-y", "--year", type=int, required=False, help="copyright year")
    parser.add_argument("-p", "--project", type=str, required=False, help="project name")
    parser.add_argument("-o", "--output-path", type=Path, required=False, help="directory to save the LICENSE file")

    args = parser.parse_args()

    license_list = [Path(item.name).stem for item in TEMPLATES_DIR.iterdir()]

    if args.list:
        print("Available license types:")
        for license in license_list:
            print(f" - {license}")
        return

    if not args.license_type or not args.author:
        parser.error("both license type and author arguments are required! Use -h flag for help.")

    if args.license_type.lower() not in license_list:
        parser.error("specified type of license does not exists!")

    create_license_file(
        license_type=args.license_type,
        author=args.author,
        year=args.year,
        project=args.project,
        output_path=args.output_path,
    )


if __name__ == "__main__":
    main()
