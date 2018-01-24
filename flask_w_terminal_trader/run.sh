#!/usr/bin/env bash

python3 schema.py
python3 seed.py
python3 controller.py
rm -rf __pycache__/
rm master.db
