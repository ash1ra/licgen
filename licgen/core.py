from datetime import datetime
from pathlib import Path
from importlib import resources

TEMPLATES_DIR = resources.files("templates")


def create_license_file(
    license_type: str,
    author: str,
    year: int | None = None,
    project: str | None = None,
    output_path: Path | None = None,
) -> None:
    year = datetime.now().year if year is None else year
    project = Path().resolve().name if project is None else project
    output_path = Path() if output_path is None else output_path
    output_path.mkdir(exist_ok=True, parents=True)

    license_file_path = TEMPLATES_DIR / f"{license_type.lower()}.txt"

    file_data = license_file_path.read_text(encoding="UTF-8")
    file_data = file_data.replace("<YEAR>", str(year))
    file_data = file_data.replace("<AUTHOR>", author)
    file_data = file_data.replace("<PROJECT>", project)

    with open(output_path / "LICENSE", "w", encoding="UTF-8") as f:
        f.write(file_data)

    print(f"LICENSE file has been successfully generated at '{output_path.absolute()}'")
