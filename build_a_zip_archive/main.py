from zipfile import ZipFile
import pathlib

def zip_folder(folder_path: str, destination_path: str, *args):
    source_path = pathlib.Path(folder_path)
    with ZipFile(destination_path, 'w') as myzip:
        if len(args) == 0:
            for path in source_path.rglob("*"):
                myzip.write(path) 
        else:
            for pattern in args:
                for path in source_path.rglob(pattern):
                    myzip.write(path) 
