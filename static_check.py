import subprocess
import sys


def _run_type_checking() -> None:
    result = subprocess.run(
        ["mypy", ".", "--strict", "--explicit-package-bases"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stdout)
        sys.exit(result.returncode)

    if result.stdout.split()[0] == "Success:":
        print("MyPy test passed")


def _run_formatting() -> None:
    result = subprocess.run(
        ["black", "--line-length=79", "."],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stdout)
        sys.exit(result.returncode)

    print("Black succesfully formatted")


def _run_import_sorting() -> None:
    result = subprocess.run(
        ["isort", "."],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stdout)
        sys.exit(result.returncode)

    print("Succesfully sorted imports")


def run_utils(
    mypy: bool = True, black: bool = True, isort: bool = True
) -> None:
    if mypy:
        _run_type_checking()

    if black:
        _run_formatting()

    if isort:
        _run_import_sorting()
