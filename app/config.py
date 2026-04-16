import os

class Config:
    SECRET_KEY = os.environ.get("APP_SECRET_KEY")

    if not SECRET_KEY:
        raise ValueError("APP_SECRET_KEY environment variable not set")