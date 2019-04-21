import pytest
import shutil
from pathlib import Path
from wasabi import Printer
import srsly

TESTS_DIR = "__tests__"
EXERCISES_DIR = "exercises"
META_FILE = "meta.json"
PYTEST_TEMPLATE = "pytestTemplate"

msg = Printer()


def format_test(name, template, test, solution):
    full_code = template.replace("${solution}", solution).replace("${test}", test)
    # Need to indent the lines to fit it into test function – can probably be less hacky
    indented = "\n".join(["    " + line for line in full_code.split("\n")])
    return "def test_{}():\n{}".format(name, indented)


def get_source_files():
    exercises_path = Path(EXERCISES_DIR)
    if not exercises_path.exists():
        msg.fail("Can't find exercises directory: {}".format(EXERCISES_DIR), exits=1)
    for py_file in exercises_path.iterdir():
        if py_file.name.startswith("test_"):
            solution_name = "solution_{}".format(py_file.name.split("test_")[1])
            solution_file = exercises_path / solution_name
            if not solution_file.exists():
                msg.warn("Didn't find solution for test: {}".format(py_file.stem))
            else:
                yield (py_file, solution_file)


def pytest_sessionstart(session):
    test_dir = Path(TESTS_DIR)
    if test_dir.exists():
        shutil.rmtree(str(test_dir))
        msg.info("Deleted existing test directory {}".format(TESTS_DIR))
    test_dir.mkdir()
    msg.good("Created test directory {}".format(TESTS_DIR))
    meta = srsly.read_json(META_FILE)
    n_files = 0
    for test_file, solution_file in get_source_files():
        with test_file.open("r", encoding="utf8") as f:
            test_code = f.read()
        with solution_file.open("r", encoding="utf8") as f:
            solution_code = f.read()
        full_code = format_test(
            test_file.stem, meta[PYTEST_TEMPLATE], test_code, solution_code
        )
        test_path = test_dir / test_file.name
        with test_path.open("w", encoding="utf8") as f:
            f.write(full_code)
        n_files += 1
    msg.good("Created {} files for pytest in {}".format(n_files, TESTS_DIR))
