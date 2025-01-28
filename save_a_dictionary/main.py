import json
from typing import Dict, Any

def load_dict(file_path: str) -> Dict[Any, Any]:
    with open(file_path, "r", encoding="utf8") as file:
        data = json.load(file)
    return data

def save_dict(file_path: str, data: Dict[Any, Any]) -> None:
    with open(file_path, "w", encoding="utf8") as file:
        json.dump(data, file)

