import requests

class WeatherAPI:
    """This code defines a class called WeatherAPI with a method called get_weather that takes a city as input and returns a list of weather information for that city.
   The get_weather method uses the OpenWeatherMap API to retrieve weather data for the specified city.
   """
    @staticmethod #When you define a method in a class and decorate it with @staticmethod, you're telling Python that the method doesn't take a self parameter
    def get_weather(city):
        api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=dd4d20110ab6f647cb8cace44511634c"
        result = requests.get(api).json()
        if result['cod'] == 200:
            codition = result['weather'][0]['main']
            description = result['weather'][0]['description']
            temp = int(result['main']['temp'] - 273.15)
            pressure = result['main']['pressure']
            humidity = result['main']['humidity']
            wind = result['wind']['speed']
            final = [codition, description, temp, pressure, humidity, wind]
            return final
       



