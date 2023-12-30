from fastapi import UploadFile
from pathlib import Path



def save_file(file: UploadFile, folder_name: str = None, filename: str = None):
    # Use the specified or default folder name
    folder_name = folder_name or "media"

    # Use the specified or original filename
    filename = filename or file.filename

    save_path = Path(folder_name) / filename
    save_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the file to the specified or default directory
    with save_path.open("wb") as buffer:
        buffer.write(file.file.read())
    return str(save_path)
