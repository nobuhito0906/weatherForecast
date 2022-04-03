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
        print("currentWeather:",data['current_weather'])
        print("weathercode:",data['current_weather']['weathercode'])
        print("daliy MaxTempature:",data['daily']['temperature_2m_max'][0])
        print("daily Min Tempature:",data['daily']['temperature_2m_min'][0])
        print("Finish")
