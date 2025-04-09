import webview
import logging
import sys

from app import flask_app 


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



run_desktop_app(flask_app)

logging.info("Application window closed.")
logging.shutdown()

