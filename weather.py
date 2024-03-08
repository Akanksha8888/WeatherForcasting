import requests

def get_weather_details(location):
    api_key = open ('key.txt').read()
    base_url = f'http://api.weatherapi.com/v1/'
    endpoint = 'current.json'
    #Building API Url
    url = f'{base_url}{endpoint}?key={api_key}&q={location}'

    #sending Get Request to API

    response = requests.get(url)

    weather_dict = {}

    #checking if request is sucessful or not
    if response.status_code==200:
        weather_data = response.json()

        weather_dict['Location'] = f'{weather_data["location"]["name"]},{weather_data["location"]["country"]}'
        weather_dict['Temperature (°C)'] = f'{weather_data["current"]["temp_c"]}'
        weather_dict['Condition'] = f'{weather_data["current"]["condition"]["text"]}'
        weather_dict['Icon'] = f'{weather_data["current"]["condition"]["icon"]}'
        weather_dict['Humidity'] = f'{weather_data["current"]["humidity"]} %'
        weather_dict['WindSpeed'] = f'{weather_data["current"]["wind_kph"]} km/hr'
        weather_dict['Pressure'] = f'{weather_data["current"]["pressure_mb"]} milibars'
        weather_dict['Precipitation'] = f'{weather_data["current"]["precip_in"]} inches'
        weather_dict['Gust'] = f'{weather_data["current"]["gust_kph"]} km/hr'
        weather_dict['UVIndex'] = f'{weather_data["current"]["uv"]}'

        #getting Icon path
        icon_location = weather_dict['Icon'].split('/')
        icon_location[-1] = icon_location[-1].replace('png', 'svg')
        icon_location = icon_location[-2] + '/' + icon_location[-1]

        # saving the icon path in weather dictionary
        weather_dict['IconLocation'] = icon_location

        weather_dict['Climate'] = f'{weather_data["current"]["condition"]["text"]}'
        return weather_dict
    else:
        return f'{response.status_code} : {response.text}'




def get_forecast_details(location):
    # weatherapi.com api key
    api_key = open(''
'key.txt').read()

    # setting the base URL for the weatherapi.com API
    base_url = f'http://api.weatherapi.com/v1/'

    # specifying the endpoint you want to use (e.g., 'current.json' for current weather)
    endpoint = 'forecast.json'

    # building the complete API URL
    url = f'{base_url}{endpoint}?key={api_key}&q={location}'

    # sending a GET request to the API
    response = requests.get(url)

    weather_dictionary = {}

    # checking if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # parsing the JSON response data
        weather_data = response.json()
        forecast_hourly_detail = list(weather_data["forecast"]["forecastday"][0]["hour"])
        for i in forecast_hourly_detail:
            # fetching the hourly time
            timestamp = i["time"]
            time = timestamp.split(" ")
            time = time[-1]

            # fetching the icon path
            icon = i["condition"]["icon"]
            icon_location = icon.split('/')
            icon_location[-1] = icon_location[-1].replace('png', 'svg')
            icon_location = icon_location[-2] + '/' + icon_location[-1]

            # getting the temperature in celsius
            temp_c = int(round(float(i["temp_c"])))
            temp_c = str(temp_c) + "°"

            weather_dictionary[time] = {'logo': icon_location, 'temp_c': temp_c}

        return weather_dictionary

    else:
        # returning an error message if the request was not successful
        return f'Error: {response.status_code} - {response.text}'









