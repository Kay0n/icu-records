import webview
import fasteners
import logging
import sys
import os
import atexit
from flask import Flask

from app import create_app 



def setup_instance_lock(flask_app):
    lock_path = flask_app.config.get('APP_LOCK_FILE') 

    lock = fasteners.InterProcessLock(lock_path)
    lock_aquired = lock.acquire(blocking=False)

    if not lock_aquired:
        logging.error(f"Another instance of {flask_app.config.get('APP_NAME')} is already running.")
        sys.exit(0)

    def release_lock():
        logging.info("Releasing application lock.")
        lock.release()

    atexit.register(release_lock) 



def run_desktop_app(flask_app: Flask) -> webview.Window:
    try:
        webview.settings["ALLOW_DOWNLOADS"] = True
        window = webview.create_window(
            'ECHO Records',
            flask_app,
            width=1200,
            height=800,
            resizable=True
        )
        
        logging.info("Application starting")
        webview.start(
            lambda w: w.maximize(),
            window, 
            debug=False, 
            http_server=True
        )

        return window

    except Exception as e:
        logging.error(f"An error occurred during application runtime: {e}")
        sys.exit(1)



# prevent startup hang caused by windows proxy setting "Automatically detect settings"
os.environ["WEBVIEW2_ADDITIONAL_BROWSER ARGUMENTS"] = "--no-proxy-server"

flask_app = create_app()

setup_instance_lock(flask_app)

run_desktop_app(flask_app)

logging.info("Application shutting down")
logging.shutdown()

