citiesTempF = { 
              'New York' : 32,
              'Boston': 75,
              'Los Angeles': 100,
              'Chicago': 50 }
citiesTempC = {key: round((value-32) *(5/9)) for (key,value) in citiesTempF.items()}
print(citiesTempC)

#---------------------------------------------------------------------------------------------------
weather = { 
              'New York' : 'snowing',
              'Boston': 'sunny',
              'Los Angeles': 'cloudy',
              'Chicago': 'sunny' }
sunnyWeather = {key:value for (key,value) in weather.items() if value == 'sunny'}
print(sunnyWeather)

#----------------------------------------------------------------------------------------------------
citiesTemp = { 
              'New York' : 32,
              'Boston': 75,
              'Los Angeles': 100,
              'Chicago': 50 }
weatherTemp = {key: ('Warm' if value>=45 else 'Cold') for (key,value) in citiesTemp.items()}
print(weatherTemp)

#----------------------------------------------------------------------------------------------------
def checkTemp(value):
  if value>=45:
    return 'very warm'
  else:
    return 'very cold'
citiesTemp = { 
              'New York' : 32,
              'Boston': 75,
              'Los Angeles': 100,
              'Chicago': 50 }
weatherTemp = {key: checkTemp(value) for (key,value) in citiesTemp.items()}
print(weatherTemp)
