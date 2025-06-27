import os
import json
import logging

class Config:
    def __init__(self, path='config/config.json'):

        # Setup logger
        log_path = os.path.join(os.path.dirname(__file__), "app.log")
        self.logger = logging.getLogger("coverletterai_logger")
        self.logger.setLevel(logging.INFO)

        # Prevent adding handlers multiple times in case of re-imports
        if not self.logger.handlers:
            # File handler
            file_handler = logging.FileHandler(log_path, mode='a')
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(file_handler)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(console_handler)

        # Open config json file
        try:
            with open(path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            self.logger.error(f"Error loading config: {str(e)}")
            data = {}

        # Set config variables
        self.GEMINI_API_KEY = data.get("GEMINI_API_KEY", "")
        self.QDRANT_API_KEY = data.get("QDRANT_API_KEY", "")
        self.QDRANT_URL = data.get("QDRANT_URL", "")

        # Log initialization
        self.logger.info("@config.py initialized successfully")