from flask import Blueprint,jsonify,send_from_directory,abort
from pathlib import Path

from services.photo_service import (get_all_photos,PHOTO_DIR,ALLOWED_EXTENSIONS)

photo_bp=Blueprint("photos",__name__)

@photo_bp.route("/api/photos",methods=["GET"])
def list_photos():
    photos=get_all_photos()
    return jsonify({
        "total":len(photos),
        "photos":photos
    })
    
@photo_bp.route("/photos/<path:filename>",methods=["GET"])
def view_photo(filename):
    file_path = (PHOTO_DIR / filename).resolve()

    if not file_path.is_relative_to(PHOTO_DIR.resolve()):
        abort(404)

    if not file_path.is_file():
        abort(404)

    if file_path.suffix.lower() not in ALLOWED_EXTENSIONS:
        abort(404)
        
    return send_from_directory(PHOTO_DIR,filename)

@photo_bp.route("/download/<path:filename>",methods=["GET"])
def download_photo(filename):
    file_path = (PHOTO_DIR / filename).resolve()

    if not file_path.is_relative_to(PHOTO_DIR.resolve()):
        abort(404)

    if not file_path.is_file():
        abort(404)

    if file_path.suffix.lower() not in ALLOWED_EXTENSIONS:
        abort(404)
        
    return send_from_directory(PHOTO_DIR,filename,as_attachmet=True)