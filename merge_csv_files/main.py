import csv
from typing import Set

def merge_files(destination, *args):
    headers: Set[str] = {}
    contents = [] 
    for path in args:
        if not isinstance(path, str):
            continue
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for header in reader:
                headers = headers | set(header)
                break
            reader = csv.DictReader(csvfile)
            for row in reader:
                contents.append(row)

    with open(destination, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, list(headers))
        writer.writerows(contents)
