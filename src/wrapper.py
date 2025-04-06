from app import app as flask_app
import webview



webview.settings["ALLOW_DOWNLOADS"] = True

webview.create_window(
    'ECHO Database', 
    flask_app,
    width=1400,
    height=850,
)

# starts window, uses default wsgi server to run flask
webview.start()
