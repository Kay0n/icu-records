import os
import sys
import configparser
import secrets
import logging
from appdirs import user_data_dir
from typing import Dict, Optional

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')



class Config:
    """
    Handles application configuration, loading from or creating a config file
    """
    APP_NAME: str = "echo-records"
    APP_AUTHOR: str = "Kayon"
    SECRET_KEY: Optional[str] = None
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    APP_DATA_DIR: str
    APP_LOCK_FILE: str
    CONFIG_FILE_PATH: str 


    def __init__(self):
        """
        Initializes Config object, sets paths, and loads/creates the secret key
        """
        self.APP_DATA_DIR = user_data_dir(self.APP_NAME, self.APP_AUTHOR)
        self.CONFIG_FILE_PATH = os.path.join(self.APP_DATA_DIR, 'config.ini')
        self.APP_LOCK_FILE = os.path.join(self.APP_DATA_DIR, 'instance.lock')
        self.SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(self.APP_DATA_DIR, 'database.sqlite')}'

        try:
            os.makedirs(self.APP_DATA_DIR, exist_ok=True)
        except OSError as e:
            logging.error(f"Fatal: Could not create data directory {self.APP_DATA_DIR}: {e}")
            sys.exit(f"Error: Failed to create necessary application data directory at {self.APP_DATA_DIR}") 

        self._load_or_create_secret_key()


    def _read_key_from_file(self, parser: configparser.ConfigParser) -> Optional[str]:
        """Reads the secret key from the config file, if it exists."""
        if not os.path.exists(self.CONFIG_FILE_PATH):
            return None
        try:
            parser.read(self.CONFIG_FILE_PATH)
            key = parser.get('Flask', 'SECRET_KEY', fallback=None)
            return key 
        except configparser.Error as e:
            logging.warning(f"Error reading config file {self.CONFIG_FILE_PATH}: {e}. Will attempt to generate a new key")
            return None 


    def _generate_and_save_key(self, parser: configparser.ConfigParser) -> str:
        """Generates a new secret key, adds it to the parser, and saves the config."""
        logging.info(f"SECRET_KEY not found or readable in {self.CONFIG_FILE_PATH}. Generating a new one")
        new_key = secrets.token_hex(16)

        if not parser.has_section('Flask'):
            parser.add_section('Flask')
        parser.set('Flask', 'SECRET_KEY', new_key)

        try:
            with open(self.CONFIG_FILE_PATH, 'w') as configfile:
                parser.write(configfile)
            logging.info(f"New configuration saved to {self.CONFIG_FILE_PATH}")
        except IOError as e:
            logging.error(f"Error writing config file {self.CONFIG_FILE_PATH}: {e}")
            logging.warning("The newly generated SECRET_KEY will be used for this session only and was NOT saved")
        
        return new_key


    def _load_or_create_secret_key(self):
        """Orchestrates loading or creating/saving the SECRET_KEY"""
        parser = configparser.ConfigParser()
        
        key = self._read_key_from_file(parser)

        if key is None:
            key = self._generate_and_save_key(parser)
        
        self.SECRET_KEY = key

