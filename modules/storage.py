import json
from pathlib import Path

storage_path = Path("storage.json")

def load_seen_items():
    if storage_path.exists():
        with open(storage_path, "r") as f:
            return set(json.load(f))
    return set()

def save_seen_items(items):
    with open(storage_path, "w") as f:
        json.dump(list(items), f)
