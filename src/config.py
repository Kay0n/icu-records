import os
import sys
import configparser
import secrets
import logging
from appdirs import user_data_dir
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


APP_NAME = "EchoDB"
APP_AUTHOR = "Kayon" 
DATA_DIR = user_data_dir(APP_NAME, APP_AUTHOR)

CONFIG_FILE_PATH = os.path.join(DATA_DIR, 'config.ini')
DATABASE_FILE_PATH = os.path.join(DATA_DIR, 'echo_database.db')
LOCK_FILE_PATH = os.path.join(DATA_DIR, 'instance.lock') 


try:
    os.makedirs(DATA_DIR, exist_ok=True)
except OSError as e:
    logging
    logging.error(f"Error creating data directory {DATA_DIR}: {e}")
    sys.exit(1)



class Config:
    """Base configuration settings."""
    SECRET_KEY = None # will be loaded or generated
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_DATA_DIR = DATA_DIR
    APP_LOCK_FILE = LOCK_FILE_PATH

def load_or_create_config():
    """
    Loads configuration from the user data directory.
    Generates a secret key if one doesn't exist and saves the config.
    Returns an instance of the Config class populated with settings.
    """
    config = Config()
    parser = configparser.ConfigParser()
    secret_key_generated = False

    if os.path.exists(CONFIG_FILE_PATH):
        try:
            parser.read(CONFIG_FILE_PATH)
            if 'Flask' in parser and 'SECRET_KEY' in parser['Flask']:
                config.SECRET_KEY = parser['Flask']['SECRET_KEY']


        except configparser.Error as e:
            logging.error(f"Error reading config file {CONFIG_FILE_PATH}: {e}")
            pass

    if not config.SECRET_KEY:
        logging.info(f"Secret key not found in {CONFIG_FILE_PATH}. Generating a new one.")
        config.SECRET_KEY = secrets.token_hex(16)
        secret_key_generated = True

        if 'Flask' not in parser:
            parser['Flask'] = {}
        parser['Flask']['SECRET_KEY'] = config.SECRET_KEY

    if secret_key_generated or not os.path.exists(CONFIG_FILE_PATH):
        try:
            with open(CONFIG_FILE_PATH, 'w') as configfile:
                parser.write(configfile)
            logging.info(f"Configuration saved to {CONFIG_FILE_PATH}")
        except IOError as e:
            logging.error(f"Error writing config file {CONFIG_FILE_PATH}: {e}")
            logging.warning(f"Key will be used for this session only")


    return config










