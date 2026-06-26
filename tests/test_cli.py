from unittest.mock import patch

import pytest
from pytest import CaptureFixture

from licgen.cli import main


def test_cli_list_available_license_types(capsys: CaptureFixture[str]) -> None:
    test_args = ["licgen", "-l"]

    with patch("sys.argv", test_args):
        main()

    captured = capsys.readouterr()
    assert "Available license types:" in captured.out


def test_cli_error_without_license_type(capsys: CaptureFixture[str]) -> None:
    test_args = ["licgen", "-a", "test"]

    with patch("sys.argv", test_args):
        with pytest.raises(SystemExit):
            main()

    captured = capsys.readouterr()
    assert "both license type and author arguments are required" in captured.err


def test_cli_error_without_author(capsys: CaptureFixture[str]) -> None:
    test_args = ["licgen", "MIT"]

    with patch("sys.argv", test_args):
        with pytest.raises(SystemExit):
            main()

    captured = capsys.readouterr()
    assert "both license type and author arguments are required" in captured.err


def test_cli_invalid_license_type(capsys: CaptureFixture[str]) -> None:
    test_args = ["licgen", "test", "-a", "test"]

    with patch("sys.argv", test_args):
        with pytest.raises(SystemExit):
            main()

    captured = capsys.readouterr()
    assert "specified type of license does not exists!" in captured.err
