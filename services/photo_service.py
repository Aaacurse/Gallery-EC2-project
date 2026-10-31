from pathlib import Path

PHOTO_DIR=Path(r"C:\Users\HP\Pictures\CS")

ALLOWED_EXTENSIONS={
    ".jpg",".jpeg",".png",".webp",".gif"
}

def get_all_photos():
    if not PHOTO_DIR.exists():
        return []
    
    photos=[
        file.name for file in PHOTO_DIR.iterdir() if file.is_file() and file.suffix.lower() in ALLOWED_EXTENSIONS
    ]
    
    return sorted(photos)