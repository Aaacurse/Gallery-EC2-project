from flask import Flask,render_template
from routes.photo_routes import photo_bp

def create_app():
    app=Flask(__name__)
    
    app.register_blueprint(photo_bp)
    
    @app.route("/")
    def home():
        return render_template("index.html")
    
    return app

app=create_app()

if __name__=="__main__":
    app.run(debug=True)