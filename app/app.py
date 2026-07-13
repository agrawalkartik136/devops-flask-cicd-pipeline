from flask import Flask, jsonify
import socket
import os
import logging
from datetime import datetime
import platform

# -----------------------------
# Logging Configuration
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# -----------------------------
# Flask Application
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Environment Variables
# -----------------------------
APP_NAME = os.getenv("APP_NAME", "DevOps Flask CI/CD Pipeline")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "Development")


# -----------------------------
# Home Endpoint
# -----------------------------
@app.route("/")
def home():
    logger.info("Home endpoint accessed")

    return jsonify({
        "application": APP_NAME,
        "description": "Production-style CI/CD Demo Project",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "status": "Running",
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "timestamp": datetime.now().isoformat()
    })


# -----------------------------
# Health Check Endpoint
# -----------------------------
@app.route("/health")
def health():
    logger.info("Health endpoint accessed")

    return jsonify({
        "status": "UP"
    })


# -----------------------------
# Readiness Check Endpoint
# -----------------------------
@app.route("/ready")
def ready():
    logger.info("Readiness endpoint accessed")

    return jsonify({
        "status": "READY"
    })


# -----------------------------
# Version Endpoint
# -----------------------------
@app.route("/version")
def version():
    logger.info("Version endpoint accessed")

    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION
    })


# -----------------------------
# Custom 404 Error
# -----------------------------
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "error": "Resource not found",
        "status": 404
    }), 404


# -----------------------------
# Main Function
# -----------------------------
if __name__ == "__main__":
    logger.info("Application Started Successfully")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False)
