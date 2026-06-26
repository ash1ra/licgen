from pathlib import Path

from licgen.core import TEMPLATES_DIR, create_license_file


def test_create_license_file(tmp_path: Path) -> None:
    license_type = "agpl-3.0"
    author = "test"
    year = 2026
    project = "test"

    create_license_file(
        license_type=license_type,
        author=author,
        year=year,
        project=project,
        output_path=tmp_path,
    )

    assert (tmp_path / "LICENSE").exists()

    with open(tmp_path / "LICENSE", "r", encoding="UTF-8") as f:
        actual_license_data = f.read()

    license_file_path = TEMPLATES_DIR / f"{license_type.lower()}.txt"

    file_data = license_file_path.read_text(encoding="UTF-8")
    file_data = file_data.replace("<YEAR>", str(year))
    file_data = file_data.replace("<AUTHOR>", author)
    file_data = file_data.replace("<PROJECT>", project)

    assert actual_license_data == file_data
