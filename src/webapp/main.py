import os
import sys

ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_FOLDER)

import uvicorn
from webapp.api.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8888)
