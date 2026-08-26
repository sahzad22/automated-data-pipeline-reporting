import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "https://fakestoreapi.com/products")
DB_URL = os.getenv("DB_URL", "sqlite:///pipeline.db")
POWERBI_ENABLED = os.getenv("POWERBI_ENABLED", "false").lower() == "true"
POWERBI_TENANT_ID = os.getenv("POWERBI_TENANT_ID")
POWERBI_CLIENT_ID = os.getenv("POWERBI_CLIENT_ID")
POWERBI_CLIENT_SECRET = os.getenv("POWERBI_CLIENT_SECRET")
POWERBI_WORKSPACE_ID = os.getenv("POWERBI_WORKSPACE_ID")
POWERBI_DATASET_ID = os.getenv("POWERBI_DATASET_ID")
