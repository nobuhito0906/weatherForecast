from openmeteo_py import Hourly, Daily, Options, OWmanager, timezones

class Open_meteo:
    
    def reqSdk(self, latitude, longitude):
        hourly = Hourly()
        
        daily = Daily()
        daily.temperature_2m_max()
        daily.temperature_2m_min()
        daily.apparent_temperature_max()
        daily.apparent_temperature_min()
        tmz = timezones.Tokyo
        options = Options(latitude, longitude,current_weather="true", timezone=tmz)

        mgr = OWmanager(options,hourly.all(),daily)
        data = mgr.get_data()
        currentWeather = data['current_weather']
        temperature = currentWeather['temperature']
        windSpeed = currentWeather['windspeed']
        weatherCode = currentWeather['weathercode']
        print("currentWeather:",currentWeather)
        print("weathercode:",weatherCode)
        print("temperature:",temperature)
        print("windSpeed:",windSpeed)
        currentText = f"現在の天気:{0} 気温:{1} 風速:{2}".format(weatherCode,temperature,windSpeed)
        print("text:",currentText)
        print("daliy MaxTempature:",data['daily']['temperature_2m_max'][0])
        print("daily Min Tempature:",data['daily']['temperature_2m_min'][0])
        print("Finish")
