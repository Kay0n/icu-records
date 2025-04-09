import webview
import fasteners
import logging
import sys
import atexit

from app import flask_app 



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


def run_desktop_app(flask_app) -> webview.Window:
    try:
        window = webview.create_window(
            'Your App Title',
            flask_app,
            width=1400,
            height=850
        )
        
        logging.info("Application starting")
        webview.start(debug=False, http_server=True) # TODO: debug on dev only

        return window

    except Exception as e:
        logging.error(f"An error occurred during application runtime: {e}")
        sys.exit(1)




setup_instance_lock(flask_app)
run_desktop_app(flask_app)


logging.info("Application shutting down")
logging.shutdown()

