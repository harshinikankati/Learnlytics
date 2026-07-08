"""
Learnlytics - Flask Application Entry Point
"""
import os
from flask import Flask
from flask_cors import CORS
from config import Config
from database.db import db
from routes.students import students_bp
from routes.summary import summary_bp
from routes.analytics import analytics_bp
from routes.powerbi import powerbi_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Extensions
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})

    # Ensure upload folder exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Register blueprints
    app.register_blueprint(students_bp, url_prefix="/api/students")
    app.register_blueprint(summary_bp,  url_prefix="/api/summary")
    app.register_blueprint(analytics_bp, url_prefix="/api/analytics")
    app.register_blueprint(powerbi_bp,  url_prefix="/api/powerbi")

    @app.route("/api/health")
    def health():
        return {"status": "ok", "version": "1.0.0"}

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
