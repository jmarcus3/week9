# This is the weather module.
# Prompts for a zip code
# and displays the current temperature
# and also sends it as a text message to your phone.

# Python 3.x
import keys
from sys import exit
from urllib.request import urlopen
from twilio.rest import Client
import json

class UserInfoCollector:
  def __init__(self):
    pass

  def promptForZipcode(self):
    zip = input("What's your zip code? ")
    if self.checkZip(zip):
      self._zip = zip
    else:
        exit(1)

  def checkZip(self, zip):
    if len(zip) != 5 or not zip.isdigit():
      print("That's not a zip code!")
      return False
    return True
      

  def promptForPhoneNumber(self):
    phone = input("What's your phone number (10 digits)? ")
    if not self.checkNumber(phone):
      exit(1)
    phone_confirmation = input("Enter it again please (10 digits)? ")
    if phone == phone_confirmation:
      self._phone = phone
    else:
      print("Those phone numbers don't match.")
      exit(1)

  def checkNumber(self, phone):
    if len(phone) != 10 or not phone.isdigit():
      print("That's not a phone number!")
      return False
    return True


# phone_confirmation = input("Enter it again please (10 digits)? ")
# if phone != phone_confirmation:
#     print("Those phone numbers don't match.")
    


# Get current temperature from OpenWeatherMap.org
class WeatherProvider:
  def getWeather(self, zip):
    url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&units=imperial&appid=" + keys.weather_api
    raw_json = urlopen(url).read()
    data = json.loads(raw_json)
    temp = data['main']['temp']
    print("It is", str(round(temp)), "degrees outside.")
    return temp
