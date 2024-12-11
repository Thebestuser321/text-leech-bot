import os

API_ID    = os.environ.get("API_ID", "26728872")
API_HASH  = os.environ.get("API_HASH", "96985c2aaea6c75408528909b7e18879")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7477897274:AAHFru67ccFY8V19XKdDflZtuLtvl_NrOc0") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
