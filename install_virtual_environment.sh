#!/usr/bin/env bash

set -e

echo ">>> Creating virtual environment using venv."
python3 -m venv .venv
echo ">>> Done! Now installing dependencies..."
.venv/bin/python -m pip install -q --upgrade pip
.venv/bin/python -m pip install -q -e .[dev]
.venv/bin/python -m pip freeze > requirements.txt
echo -e ">>> Installed! Activating using \n>>> . .venv/bin/activate"