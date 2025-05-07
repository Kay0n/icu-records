import sys
import logging
from datetime import datetime, date, time
from flask import Flask

from config import Config
from database import database
from routes import register_routes




def create_app() -> Flask:

    flask_app: Flask = Flask(__name__)

    config: Config = Config()
    flask_app.config.from_object(config)

    database.init_app(flask_app)
    
    with flask_app.app_context():
        import database_model
        try:
            database.create_all()
            logging.info("Database tables checked/created successfully.")
        except Exception as e:
            logging.error(f"Error creating database tables: {e}")
            sys.exit(1)

    register_routes(flask_app)

    flask_app.add_template_filter(_jinja2_filter_fmt, name="fmt")
    
    return flask_app



# custom jninja filters
def format_value(value):
    """Helper to format values for display, handling None."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if isinstance(value, (date, time, datetime)):
        return value.strftime("%Y-%m-%d" if isinstance(value, date) else "%H:%M")
    return str(value)



def _jinja2_filter_fmt(value):
    return format_value(value)
