import sys
import logging
from datetime import datetime, date, time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config



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



flask_app = Flask(__name__)

config: Config = Config()
flask_app.config.from_object(config)

database = SQLAlchemy(flask_app)

# import models and forms after db is initialized
from models import PatientRecord
from forms import RecordForm

with flask_app.app_context():
    try:
        database.create_all()
        logging.info("Database tables checked/created successfully.")
    except Exception as e:
        logging.error(f"Error creating database tables: {e}")
        sys.exit(1)

import routes



@flask_app.template_filter("fmt")
def _jinja2_filter_fmt(value):
    return format_value(value)



if __name__ == "__main__":
    flask_app.run()  # development only
