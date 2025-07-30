import json
import os
from typing import Dict, List, Optional
from config import DB_PATH

def readJson(filename: str) -> Dict:
    path = os.path.join(DB_PATH, filename)
    try:
        with open(path, "r", encoding="utf-8") as cf:
            return json.load(cf)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def writeJson(data: Dict, filename: str) -> None:
    path = os.path.join(DB_PATH, filename)
    with open(path, "w", encoding="utf-8") as cf:
        json.dump(data, cf, indent=4)

def updateJson(data: Dict, path_keys: Optional[List[str]] = None, filename: str = "libros.json") -> bool:
    currentData = readJson(filename)

    if not path_keys:
        currentData.update(data)
    else:
        current = currentData
        for key in path_keys[:-1]:
            current = current.setdefault(key, {})
        current.setdefault(path_keys[-1], {}).update(data)

    writeJson(currentData, filename)
    return True

def deleteJson(path_keys: List[str], filename: str) -> bool:
    data = readJson(filename)
    if not data:
        return False

    current = data
    for key in path_keys[:-1]:
        if key not in current:
            return False
        current = current[key]

    if path_keys[-1] in current:
        del current[path_keys[-1]]
        writeJson(data, filename)
        return True
    return False

def initializeJson(initialStructure: Dict, filename: str) -> None:
    path = os.path.join(DB_PATH, filename)
    if not os.path.isfile(path):
        writeJson(initialStructure, filename)
    else:
        currentData = readJson(filename)
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson(currentData, filename)

