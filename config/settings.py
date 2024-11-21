import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# # Dynamically determine the root folder based on the file location
ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Optionally, define paths to other key directories in the project
SRC_FOLDER = os.path.join(ROOT_FOLDER, "src")
BACKEND_FOLDER = os.path.join(SRC_FOLDER, "backend")
FRONTEND_FOLDER = os.path.join(SRC_FOLDER, "frontend")

# print(f"ROOT            :{ROOT_FOLDER}")
# print(f"SRC_FOLDER      :{SRC_FOLDER}")
# print(f"BACKEND_FOLDER  :{BACKEND_FOLDER}")
# print(f"FRONTEND_FOLDER :{FRONTEND_FOLDER}")
