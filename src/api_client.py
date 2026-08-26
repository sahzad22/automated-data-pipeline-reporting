import requests
from tenacity import retry, stop_after_attempt, wait_exponential
from .config import API_URL

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8))
def fetch_products():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError("API response must be a list of product records")
    return payload
