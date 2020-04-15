import pytest
import shutil
from pathlib import Path
from wasabi import msg
import srsly
import shutil
from spacy.tokens.underscore import Underscore


TESTS_DIR = "__tests__"
EXERCISES_DIR = "exercises"
META_FILE = "meta.json"
PYTEST_TEMPLATE = "pytestTemplate"
LANG_CLI_ARG = "lang"
GENERAL_TEST = "test_general.py"


@pytest.fixture(scope="module", autouse=True)
def clean_underscore():
    # reset the Underscore object after the test, to avoid having state copied across tests
    yield
    Underscore.doc_extensions = {}
    Underscore.span_extensions = {}
    Underscore.token_extensions = {}



def format_test(name, template, test, solution):
    full_code = template.replace("${solution}", solution).replace("${test}", test)
    # Need to indent the lines to fit it into test function – can probably be less hacky
    indented = "\n".join(["    " + line for line in full_code.split("\n")])
    return f"def test_{name}():\n{indented}"


def get_source_files(lang):
    exercises_path = Path(EXERCISES_DIR)
    if not exercises_path.exists():
        msg.fail(f"Can't find exercises directory: {EXERCISES_DIR}", exits=1)
    for lang_path in exercises_path.iterdir():
        if lang_path.is_dir():
            lang_name = lang_path.stem
            if lang and lang_name != lang:
                continue
            for py_file in lang_path.iterdir():
                if py_file.name.startswith("test_"):
                    solution_name = f"solution_{py_file.name.split('test_')[1]}"
                    solution_file = lang_path / solution_name
                    if not solution_file.exists():
                        if py_file.name == GENERAL_TEST:
                            yield (lang_name, py_file, None)
                        else:
                            msg.warn(f"Didn't find solution for test: {py_file.stem} ({lang_path})")
                    else:
                        yield (lang_name, py_file, solution_file)


def pytest_addoption(parser):
    parser.addoption(f"--{LANG_CLI_ARG}", action="store", dest=LANG_CLI_ARG)


def pytest_sessionstart(session):
    lang = session.config.getoption(LANG_CLI_ARG)
    if lang:
        msg.info(f"Running only tests for '{lang}'")
    test_dir = Path(TESTS_DIR)
    if test_dir.exists():
        shutil.rmtree(str(test_dir))
        msg.info(f"Deleted existing test directory {TESTS_DIR}")
    test_dir.mkdir()
    msg.good(f"Created test directory {TESTS_DIR}")
    meta = srsly.read_json(META_FILE)
    n_files = 0
    for test_lang, test_file, solution_file in get_source_files(lang):
        test_root = test_dir / test_lang
        if not test_root.exists():
            test_root.mkdir()
            init_path = test_root / "__init__.py"
            init_path.touch()
        if not solution_file:  # general test file, just copy it over
            shutil.copy(str(test_file), str(test_root / test_file.name))
            n_files += 1
            continue
        with test_file.open("r", encoding="utf8") as f:
            test_code = f.read()
        with solution_file.open("r", encoding="utf8") as f:
            solution_code = f.read()
        full_code = format_test(
            test_file.stem, meta[PYTEST_TEMPLATE], test_code, solution_code
        )
        test_path = test_root / test_file.name
        with test_path.open("w", encoding="utf8") as f:
            f.write(full_code)
        n_files += 1
    msg.good(f"Created {n_files} files for pytest in {TESTS_DIR}")
