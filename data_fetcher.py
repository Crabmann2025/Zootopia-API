import os
import requests
from dotenv import load_dotenv

# ------------------ Load Environment ------------------
load_dotenv()  # Loads variables from the .env file
API_KEY = os.getenv("API_KEY")  # Retrieves the API_KEY from the environment
API_URL = "https://api.api-ninjas.com/v1/animals?name={}"

# ------------------ Data Fetcher ------------------

def fetch_data(animal_name):
    """
    Fetches data for an animal from API Ninja.
    Returns: a list of dictionaries, each describing an animal:
    {
        'name': ...,
        'taxonomy': {...},
        'locations': [...],
        'characteristics': {...}
    }
    """
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL.format(animal_name), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching API: {response.status_code}")
        return []
