from flask import Blueprint,jsonify,send_from_directory,abort,send_file
from pathlib import Path
import zipfile
import io

from services.photo_service import (get_all_photos,PHOTO_DIR,ALLOWED_EXTENSIONS,get_all_photos_paths)

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
        
    return send_from_directory(PHOTO_DIR,filename,as_attachment=True)

@photo_bp.route("/download-all")
def download_all():
    photos=get_all_photos_paths()
    
    if not photos:
        return{"error": "No Photos available"},404
    
    zip_buffer=io.BytesIO()
    
    with zipfile.ZipFile(
        zip_buffer,
        mode='w',
        compression=zipfile.ZIP_DEFLATED
    ) as zip_file:
        
        for photo in photos:
            relative_path=photo.relative_to(PHOTO_DIR)
            zip_file.write(photo,arcname=relative_path.as_posix())
            
    zip_buffer.seek(0)
    
    return send_file(
        zip_buffer,
        mimetype="application/zip",
        as_attachment=True,
        download_name="photo_gallery.zip"
    )
            