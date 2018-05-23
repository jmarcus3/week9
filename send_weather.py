# Prompts for a zip code
# and displays the current temperature
# and also sends it as a text message to your phone.

# Python 3.x
import keys
from sys import exit
from urllib.request import urlopen
from twilio.rest import Client
import json
import weather


# Send as text message

def main():
  user_info_collector = weather.UserInfoCollector()
  weather_provider = weather.WeatherProvider()
  user_info_collector.promptForZipcode()
  temp = weather_provider.getWeather(user_info_collector._zip)
  user_info_collector.promptForPhoneNumber()

  print()
  print("(Press CTRL-C now if you do not want to send a text message)")


  client = Client(keys.account_sid, keys.auth_token)

  sms_body = "It is " + str(round(temp)) + " degrees outside."
  message = client.messages.create(
                                body= sms_body,
                                from_= keys.from_number,
                                to='+1' + user_info_collector._phone
                            )

  # If the message was successfully sent, the message object
  # will have a "sid" property that you can access:
  print("Message Sent! Tracking ID is:", message.sid)

if __name__ == "__main__":
  main()