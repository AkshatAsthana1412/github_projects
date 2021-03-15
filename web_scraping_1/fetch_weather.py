from bs4 import BeautifulSoup
import requests
import csv
import time
from argparse import ArgumentParser

'''Command line interface'''
parser = ArgumentParser(prog='weather', description='Displays weather conditions of American cities over the next 3 days')
parser.add_argument('cities', action='store', nargs='+', help='accepts one or more American city names')
parser.add_argument('--output_path', action='store', help='path to the output file', nargs='?', default='./weather.csv')
args = parser.parse_args()

'''returns the wikidata ID for the city with name <city_name>'''
def get_city_code(city_name):
  wiki_data_url = 'https://www.wikidata.org/w/api.php'
  args = {'sites':'enwiki', 'titles':city_name, 'format':'json', 'action': 'wbgetentities'}
  response = requests.get(wiki_data_url, args)
  city_id = list(response.json()['entities'].keys())[0]
  return city_id

'''returns latitude and longitude for the given city_code(wikidata ID)'''
def get_lat_lon(city_code):
  url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + city_code
  headers = {
      'x-rapidapi-key': "f557fe0f6bmsh16f92a80a102f99p164ef1jsn688975d908f9",
      'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
      }
  lat, lon = None, None
  try:
    time.sleep(3)
    response = requests.get(url, headers=headers)
    json_response = response.json()
    response.raise_for_status()
    # print(json_response)
    lat = json_response['data']['latitude']
    lon = json_response['data']['longitude']
  except:
    print(f'Could not fetch data for {city_code}')
  return (lat, lon)


if __name__ == '__main__':
  output_file = args.output_path
  cities = args.cities
  with open(output_file, 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['City', 'Period', 'Description', 'Temperature'])
    for city in cities:
      city_code = get_city_code(city)
      lat, lon = get_lat_lon(city_code)
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
        print(f'could not fetch data for {city}')
      else:
        print(f'{city} weather fetched successfuly!')
  print('Success!')