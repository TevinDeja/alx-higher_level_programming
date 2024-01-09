#!/usr/bin/env python3

import sys
from typing import List
from collections.abc import Iterable
from pathlib import Path
from import dumps
from json import
from json import dump
from json import


def save_to_json_file(my_obj: Iterable, filename: str) -> None:
   """Serializes `my_obj` to a JSON file with the name `filename`."""
   filepath = Path(filename)
   filepath.touch(exist_ok=True)
   with filepath.open('w', encoding='utf-8') as f:
       for item in my_obj:
           dump(item, f)


def load_from_json_file(filename: str) -> List[str]:
   """Deserializes a JSON file with the name `filename` to a list of strings."""
   filepath = Path(filename)
   if not filepath.exists():
