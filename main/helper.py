from django.conf import settings
import requests
from datetime import datetime

def get_weather_data(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/onecall'

    params = {
        'lat': lat,
        'lon': lon,
        'exclude': 'hourly',
        'appid': '29037181345894668cb62c21bdf048ec',
        'units': 'metric',
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return

    json_response = response.json()

    date_dict = {
        'day1_dt': json_response['daily'][0]['dt'],
        'day2_dt': json_response['daily'][1]['dt'],
        'day3_dt': json_response['daily'][2]['dt'],
        'day4_dt': json_response['daily'][3]['dt'],
        'day5_dt': json_response['daily'][4]['dt'],
        }

    day1_date_timestamp = datetime.fromtimestamp(date_dict['day1_dt'])
    day1_date_format = day1_date_timestamp.strftime("%d.%m.%Y")

    day2_date_timestamp = datetime.fromtimestamp(date_dict['day2_dt'])
    day2_date_format = day2_date_timestamp.strftime("%d.%m.%Y")

    day3_date_timestamp = datetime.fromtimestamp(date_dict['day3_dt'])
    day3_date_format = day3_date_timestamp.strftime("%d.%m.%Y")

    day4_date_timestamp = datetime.fromtimestamp(date_dict['day4_dt'])
    day4_date_format = day4_date_timestamp.strftime("%d.%m.%Y")

    day5_date_timestamp = datetime.fromtimestamp(date_dict['day5_dt'])
    day5_date_format = day5_date_timestamp.strftime("%d.%m.%Y")

    temp_delta = {
        'day1_delta': (json_response['daily'][0]['temp']['night']) - 
            (json_response['daily'][0]['temp']['morn']),
        'day2_delta': (json_response['daily'][1]['temp']['night']) - 
            (json_response['daily'][1]['temp']['morn']),
        'day3_delta': (json_response['daily'][2]['temp']['night']) - 
            (json_response['daily'][2]['temp']['morn']),
        'day4_delta': (json_response['daily'][3]['temp']['night']) - 
            (json_response['daily'][3]['temp']['morn']),
        'day5_delta': (json_response['daily'][4]['temp']['night']) - 
            (json_response['daily'][4]['temp']['morn']),
        }
    
    temp_delta_dict_min_value = min(temp_delta.values())

    key_list = list(temp_delta.keys())

    val_list = list(temp_delta.values())

    min_value_delta_temp = key_list[val_list.index(temp_delta_dict_min_value)]

    if min_value_delta_temp == 'day1_delta':
        final_min_temp_day = day1_date_format
    elif min_value_delta_temp == 'day2_delta':
        final_min_temp_day = day2_date_format
    elif min_value_delta_temp == 'day3_delta':
        final_min_temp_day = day3_date_format
    elif min_value_delta_temp == 'day4_delta':
        final_min_temp_day = day4_date_format
    elif min_value_delta_temp == 'day5_delta':
        final_min_temp_day = day5_date_format

    min_pressure = {
        'day1_pressure': json_response['daily'][0]['pressure'],
        'day2_pressure': json_response['daily'][1]['pressure'],
        'day3_pressure': json_response['daily'][2]['pressure'],
        'day4_pressure': json_response['daily'][3]['pressure'],
        'day5_pressure': json_response['daily'][4]['pressure'],
        }
    
    max_pressure_value = max(min_pressure.values())

    weather_data = {
        'day1_dt': day1_date_format,
        'day1_temp_current': json_response['daily'][0]['temp']['day'],
        'day1_press_current': json_response['daily'][0]['pressure'],
        'day1_temp_morn': json_response['daily'][0]['temp']['morn'],
        'day1_temp_night': json_response['daily'][0]['temp']['night'],
        'day1_delta': abs(round((json_response['daily'][0]['temp']['night']) - 
            (json_response['daily'][0]['temp']['morn']), 2)),
        'day2_dt': day2_date_format,
        'day2_temp_current': json_response['daily'][1]['temp']['day'],
        'day2_press_current': json_response['daily'][1]['pressure'],
        'day2_temp_morn': json_response['daily'][1]['temp']['morn'],
        'day2_temp_night': json_response['daily'][1]['temp']['night'],
        'day2_delta': abs(round((json_response['daily'][1]['temp']['night']) - 
            (json_response['daily'][1]['temp']['morn']), 2)),
        'day3_dt': day3_date_format,
        'day3_temp_current': json_response['daily'][2]['temp']['day'],
        'day3_press_current': json_response['daily'][2]['pressure'],
        'day3_temp_morn': json_response['daily'][2]['temp']['morn'],
        'day3_temp_night': json_response['daily'][2]['temp']['night'],
        'day3_delta': abs(round((json_response['daily'][2]['temp']['night']) - 
            (json_response['daily'][2]['temp']['morn']), 2)),
        'day4_dt': day4_date_format,
        'day4_temp_current': json_response['daily'][3]['temp']['day'],
        'day4_press_current': json_response['daily'][3]['pressure'],
        'day4_temp_morn': json_response['daily'][3]['temp']['morn'],
        'day4_temp_night': json_response['daily'][3]['temp']['night'],
        'day4_delta': abs(round((json_response['daily'][3]['temp']['night']) - 
            (json_response['daily'][3]['temp']['morn']), 2)),
        'day5_dt': day5_date_format,
        'day5_temp_current': json_response['daily'][4]['temp']['day'],
        'day5_press_current': json_response['daily'][4]['pressure'],
        'day5_temp_morn': json_response['daily'][4]['temp']['morn'],
        'day5_temp_night': json_response['daily'][4]['temp']['night'],
        'day5_delta': abs(round((json_response['daily'][4]['temp']['night']) - 
            (json_response['daily'][4]['temp']['morn']), 2)),
        'min_temp_delta_day': final_min_temp_day,
        'min_temp_delta_value': abs(round(temp_delta_dict_min_value, 2)),
        'max_pressure': max_pressure_value,
        }

    return weather_data

    

