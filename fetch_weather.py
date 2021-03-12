from bs4 import BeautifulSoup
import requests
import csv
import time
from argparse import ArgumentParser

parser = ArgumentParser(prog='weather', description='Displays weather conditions of cities over the next 3 days')
parser.add_argument('cities')
wiki_data_url = 'https://www.wikidata.org/w/api.php'

cities = ['Chicago', 'New York City', 'Los Angeles', 'Atlanta']
city_ids = []
for city in cities: 
  args = {'sites':'enwiki', 'titles':city, 'format':'json', 'action': 'wbgetentities'}
  response = requests.get(wiki_data_url, args)
  city_ids.extend(list(response.json()['entities'].keys()))
# print(city_ids)
city_ids_dict = dict(zip(city_ids, cities))
print(city_ids_dict)


coordinates = dict()
for code in city_ids_dict.keys():
  url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + code
  print(url)
  headers = {
      'x-rapidapi-key': "f557fe0f6bmsh16f92a80a102f99p164ef1jsn688975d908f9",
      'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
      }

  try:
    response = requests.get(url, headers=headers)
    json_response = response.json()
    response.raise_for_status()
    # print(json_response)
    lat = json_response['data']['latitude']
    lon = json_response['data']['longitude']
    coordinates[city_ids_dict[code]] = (lat, lon)
    time.sleep(5)
  except Exception as e:
    print(e)

print(coordinates)

# page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
with open('weather_data.csv', 'w') as file:
  csv_writer = csv.writer(file)
  csv_writer.writerow(['City', 'Period', 'Description', 'Temperature'])
  for city in coordinates.keys():
    lat, lon = coordinates[city][0], coordinates[city][1]
    args = {'lat' : lat, 'lon' : lon}
    try:
      page = requests.get('https://forecast.weather.gov/MapClick.php', params=args)
      print(page.status_code)
      soup = BeautifulSoup(page.content, 'html.parser')
      seven_day_fc = soup.find(id="seven-day-forecast-container")
      days_data = seven_day_fc.select("li.forecast-tombstone div.tombstone-container")

      for day in days_data:
        period = day.find(class_='period-name').get_text()
        desc = day.select('p > img')[0]['title']
        temp = day.find(class_ = 'temp').get_text()
        csv_writer.writerow([city, period, desc, temp])
    except Exception as e:
      print(e)
print('Success!')