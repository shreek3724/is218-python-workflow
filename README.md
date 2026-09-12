# IS218 Assignment 1 Issue 1 README File
This project involves learning how to use the command line to update, push and pull changes to Github, as well as navigate using python to create tests and learning to navigate the system.

## README Update - Part of Issue 4, Assignment 1

# Repository URL
https://github.com/shreek3724/is218-python-workflow
# Python Version
Python 3.12.14
# Passing Test Count
2 Passed in 0.01s
# README.md file description
Contains descriptions of other files in the project, all within "class-project" within "projects" under "user" folder. The file also contains python version, set up command information, and commit notes and results for furture reference.
# .gitignore file description
This file tells Git while files or folders to ignore when updating/commiting changes to Github.
# requirements.txt file description
This file contains external files/software tools that are used in this project, and must be downloaded in order for the project to run as intended.
# app.py file description
This is the main application file, where the program logic, and given/original, and personal test functions to add integers is.
# tests/test_app.py description
This file contains tests to test the app.py code, resulting in passes, and fails. 
# Recording Python version & Set Up Commands 
python -m pip install -r requirements.txt
python -m pytest --version
python --version
git check-ignore .venv/
git ls-files .venv

((.venv) ) macbook-air-4:class-project shreejitha$ python -m pytest --version
pytest 8.4.2
((.venv) ) macbook-air-4:class-project shreejitha$ python --version
Python 3.12.14
((.venv) ) macbook-air-4:class-project shreejitha$ git check-ignore .venv/
.venv/
((.venv) ) macbook-air-4:class-project shreejitha$ git ls-files .venv
((.venv) ) macbook-air-4:class-project shreejitha$ 

# If opening a new terminal session, reactivate the environment.
source .venv/bin/activate 
From class-projects folder. Navigate to it using cd.
cd ~/projects/class-project
code .

# If running a test from the repository root, use:
python -m pytest
Fromt the class-projects folder.

# Environment Set Up (Already Done)
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

# Pushing Changes (Method from Assignment 0 & 1)
git status
git diff
git add ____add file names here____
git diff --staged
git commit -m "Commit Title #issueNumber"
git push