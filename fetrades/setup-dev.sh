#!/bin/bash
set -e

./setup.sh

source .venv/bin/activate
pip install -r requirements-dev.txt
deactivate
