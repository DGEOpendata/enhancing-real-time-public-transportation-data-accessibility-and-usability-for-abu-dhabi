python
import requests
import json

# URL for the real-time public transportation data API
api_url = "https://api.abudhabi.transport/data"

# Query parameters (example for fetching bus routes)
params = {
    'transport_mode': 'bus',
    'filter': 'real-time',
    'language': 'en'
}

# Fetch real-time public transportation data
def fetch_real_time_data(api_url, params):
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Fetch data using the API
    real_time_data = fetch_real_time_data(api_url, params)

    # Check if data fetching was successful
    if real_time_data:
        print(json.dumps(real_time_data, indent=4))

        # Example: Extract and print bus routes and estimated arrival times
        for route in real_time_data.get('routes', []):
            print(f"Route: {route['route_number']} - Estimated Arrival: {route['estimated_arrival']}")
    else:
        print("Failed to fetch real-time public transportation data.")
