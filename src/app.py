import os
from datetime import datetime, date, time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_instance_folder():
    try:
        os.makedirs(os.path.join(basedir, "instance"))
    except OSError:
        pass


def create_database_tables(flask_app, database):
    with flask_app.app_context():
        try:
            database.create_all()
            print("Database tables checked/created successfully.")
        except Exception as e:
            print(f"Error creating database tables: {e}")


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



app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback-key")
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "instance", "records.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


create_instance_folder()
db = SQLAlchemy(app)


# import models and forms after db is initialized
from models import PatientRecord
from forms import RecordForm

create_database_tables(app, db)

import routes





@app.template_filter("fmt")
def _jinja2_filter_fmt(value):
    return format_value(value)





if __name__ == "__main__":
    app.run()  # development only
