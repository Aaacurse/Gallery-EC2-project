from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(override=True)

PHOTO_DIR=Path(os.getenv("PHOTO_DIR","photos")).expanduser().resolve()

ALLOWED_EXTENSIONS={
    ".jpg",".jpeg",".png",".webp",".gif"
}

def get_all_photos():
    if not PHOTO_DIR.exists():
        return []
    
    photos=[
        file.relative_to(PHOTO_DIR).as_posix() for file in PHOTO_DIR.rglob("*") if file.is_file() and file.suffix.lower() in ALLOWED_EXTENSIONS
    ]
    
    return sorted(photos)

def get_all_photos_paths():
    if not PHOTO_DIR.exists():
        return []
    
    return [
        file
        for file in PHOTO_DIR.rglob("*")
        if file.is_file() and file.suffix.lower() in ALLOWED_EXTENSIONS
    ]