import requests
from datetime import datetime
from pprint import pprint

api_key = '6727ead5dfa64ae630e4a50c6eda4dcb'

lat = 37.7749
lon = -122.4194

units = 'imperial'

api_url = (
    f'https://api.openweathermap.org/data/2.5/forecast'
    f'?lat={lat}&lon={lon}&units={units}&appid={api_key}'
)

def fetch_weather_forecast(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'An error occurred: {err}')
    return None

def process_forecast_data(forecast_data):
    print(f'5-day weather forecast for San Francisco (in 3-hour intervals):\n')

    daily_data = {}

    for forecast in forecast_data.get('list', []):
        date = datetime.fromtimestamp(forecast['dt']).strftime('%m/%d/%Y')
        temp = forecast['main']['temp']
        humidity = forecast['main']['humidity']

        if date not in daily_data:
            daily_data[date] = {'total_temp': 0, 'total_humidity': 0, 'count': 0}

        daily_data[date]['total_temp'] += temp
        daily_data[date]['total_humidity'] += humidity
        daily_data[date]['count'] += 1

    for date, data in daily_data.items():
        avg_temp = data['total_temp'] / data['count']
        avg_humidity = data['total_humidity'] / data['count']

        print(f'Date: {date}')
        print(f'  Avg Temperature: {avg_temp:.2f}°F')
        print(f'  Avg Humidity: {avg_humidity:.2f}%\n')

def main():
    forecast_data = fetch_weather_forecast(api_url)
    if forecast_data:
        process_forecast_data(forecast_data)

if __name__ == '__main__':
    main()
