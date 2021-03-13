from bs4 import BeautifulSoup
import requests
import csv
import time
from argparse import ArgumentParser

parser = ArgumentParser(prog='weather', description='Displays weather conditions of American cities over the next 3 days')
parser.add_argument('cities', action='store', nargs='+', help='accepts one or more American city names')
parser.add_argument('--output_path', action='store', help='path to the output file', nargs='?', default='./weather.csv')
args = parser.parse_args()

wiki_data_url = 'https://www.wikidata.org/w/api.php'


def get_city_codes(cities):
  city_ids = []
  for city in cities: 
    args = {'sites':'enwiki', 'titles':city, 'format':'json', 'action': 'wbgetentities'}
    response = requests.get(wiki_data_url, args)
    city_ids.extend(list(response.json()['entities'].keys()))

  city_ids_dict = dict(zip(city_ids, cities))
  return city_ids_dict

def get_lat_lon(cities, get_city_codes):
    city_ids_dict = get_city_codes(cities)
    coordinates = dict()
    for code in city_ids_dict.keys():
      url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + code
      # print(url)
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
      except:
        print(f'Could not fetch data for {city_ids_dict[code]}')
        continue
    return coordinates


output_file = args.output_path
cities = args.cities
print(cities)
coordinates = get_lat_lon(cities, get_city_codes)
with open(output_file, 'w') as file:
  csv_writer = csv.writer(file)
  csv_writer.writerow(['City', 'Period', 'Description', 'Temperature'])
  for city in coordinates.keys():
    lat, lon = coordinates[city][0], coordinates[city][1]
    args = {'lat' : lat, 'lon' : lon}
    try:
      page = requests.get('https://forecast.weather.gov/MapClick.php', params=args)
      soup = BeautifulSoup(page.content, 'html.parser')
      seven_day_fc = soup.find(id="seven-day-forecast-container")
      days_data = seven_day_fc.select("li.forecast-tombstone div.tombstone-container")

      for day in days_data:
        period = day.find(class_='period-name').get_text()
        desc = day.select('p > img')[0]['title']
        temp = day.find(class_ = 'temp').get_text()
        csv_writer.writerow([city, period, desc, temp])
    except Exception as e:
      print(f'Can fetch weather conditions for american cities only! {city} is not in America')
    else:
      print(f'{city} weather fetched successfuly!')
print('Success!')