# Test Python Project

## Initialization

1) Create project directory with `mkdir projectname`

2) Initialize a local git repo with `git init`

3) Create a virtual env using `python -m venv venv`

4) Activate the venv `venv/scripts/activate.bat` or `activate.ps1` if powershell

5) Add your code, extra files like README.md. 

6) Stage changes using the plus icon in vs code.

7) Perform first commit.

8) (OPTIONAL) Create an empty repository on github, and copy and execute instructions to push the local repo.

## Tests

Unit Testing

- Code that is testable is more maintainable, and can be changed easily, without fear.

- Tests are executable documentation.
  - They have a description - What the test is
  - They show what the input/requirements are - Preconditions
  - They assert what the output/effect is - Postconditions

  Ex. A function that downloads a file. 
  Precondition - File not found in local
  Run the function - Download a file
  Postcondition - File is found

- TDD - Test Driven Development
  A style of programming where you design and write your test before writing the code that passes the test.
  It forces you to break down the system into testable chunks - `units`.
  Unit tests don't require dependencies of the overall system - they mock out dependencies for testing.

## Setup for Pytest

Either flat files - tests/code in same directory

Or create a `setup.py` file which is the standard way of turning your code into an installable library.
We install the code, and the tests will be able to import the functions like any other python package.
 
`setup.py`
```python
from setuptools import setup
setup(
    name='testpyproj', # name with which we pip install
    version='0.0.1',
    description='Test project',
    package_dir={'': 'src'}, 
)
```

Install the package while allowing updates to the installed package by `pip install -e .` in the root folder.

Package under `src` with tests nested inside the package.
```
src/
├── mypackage
│   ├── script.py
│   └── tests
│       └── test_script.py
```

Run the tests by using `pytest` in the root folder.
For more verbose output, run `pytest -v`.

