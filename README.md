# LeetCode

This repository consists of solutions to Leetcode problems for personal documentation and public learning use.

## Environment setup

0. Install python3 via documentation.
Documentation: https://www.python.org/downloads/

1. Install poetry using: "curl -sSL https://install.python-poetry.org | python3 -"
Documentation: https://python-poetry.org/docs/#installing-with-the-official-installer
Note: This is a package / dependency manager for python.

2. poetry install
Note: Sets up the dependencies and environment based on toml and lock files that track dependencies.


## Running source code

1. Change directory into the "leetcode-solutions" folder.

2. run "poetry run python3 -m src.foldername.filename"
[example: "poetry run python3 -m src.solutions.wordsearch"] to run the wordsearch.py file in the src/solutions folder.


## Running the whole test package

1. Change directory into the "leetcode-solutions" folder.

2. run "poetry run pytest"
Note: This runs all of the unittests in the tst package.

## Running individual test files

1. change directory into the "leetcode-solutions" folder.


2. run "poetry run pytest tst/solutions/test_file_name.py"
[example: "poetry run pytest tst/solutions/test_wordsearch.py"] to run the test_wordsearch.py file in the tst/solutions folder.
