import requests
from .config import (POWERBI_ENABLED, POWERBI_TENANT_ID, POWERBI_CLIENT_ID,
    POWERBI_CLIENT_SECRET, POWERBI_WORKSPACE_ID, POWERBI_DATASET_ID)

def trigger_powerbi_refresh():
    if not POWERBI_ENABLED:
        return {"status": "SKIPPED", "reason": "POWERBI_ENABLED=false"}
    token_url = f"https://login.microsoftonline.com/{POWERBI_TENANT_ID}/oauth2/v2.0/token"
    token = requests.post(token_url, data={
        "grant_type": "client_credentials",
        "client_id": POWERBI_CLIENT_ID,
        "client_secret": POWERBI_CLIENT_SECRET,
        "scope": "https://analysis.windows.net/powerbi/api/.default"
    }, timeout=30)
    token.raise_for_status()
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{POWERBI_WORKSPACE_ID}/datasets/{POWERBI_DATASET_ID}/refreshes"
    response = requests.post(url,
        headers={"Authorization": f"Bearer {token.json()['access_token']}"}, timeout=30)
    response.raise_for_status()
    return {"status": "TRIGGERED"}
