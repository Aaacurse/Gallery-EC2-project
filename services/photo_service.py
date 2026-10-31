from pathlib import Path

PHOTO_DIR=Path(r"C:\Users\HP\Pictures\CS")

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