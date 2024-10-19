import requests, json
from pprint import pprint

# Path to the image file
image_1 = "/Users/sawan/Projects/Berkeley/CalHacks11/PlantPedia-Backend/plant.jpg"

# Project parameter
project = 'all'  # You can change this to 'weurope', 'canada', etc.

# API endpoint and API key
api_key = '2b10bLLpIoxQ0zoiD6XKS56KTe'
url = f'https://my-api.plantnet.org/v2/identify/{project}?api-key={api_key}'

# Form data
data = {
    'organs': 'auto'
}

# Prepare the files payload
files = {
    'images': open(image_1, 'rb')
}

try:
    # Make the POST request
    response = requests.post(url, files=files, data=data)
    
    # Raise an exception for HTTP error codes
    response.raise_for_status()
    
    # Print the status code
    print('status', response.status_code)
    
    # Pretty-print the JSON response
    pprint(response.json())

    resp = response.json()

    print(resp['bestMatch'])

    scientific_name = resp['results']

    print(scientific_name)

    # r = requests.get('https://trefle.io/api/v1/plants?token=J7H_C723reHrmBhe0dZjZRQlxRCn3SARRQrsoPl-780')

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # HTTP error
except Exception as err:
    print(f'An error occurred: {err}')  # Other errors
finally:
    # Close the file
    files['images'].close()

