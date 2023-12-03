import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import json
import time
import matplotlib
matplotlib.use('TkAgg')

c = input("ведите название вашего города на английском: ")
today = time.strftime('%Y-%m-%d')
in_7_days = time.strftime('%Y-%m-%d', time.localtime(time.time() + 7 * 24 * 60 * 60))
r = requests.get(
    f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{c.capitalize()}/{today}/{in_7_days}?key=LXWJM2GK64V6YYL3VLF635DJN')
data = r.json()
# f = open('data.json', 'w')
# json.dump(data, f, indent=2)

plt.style.use('_mpl-gallery')

weekly_temperature = []  # celsium
weekly_feels = []  # celsium
weekly_humidity = []  # %
weekly_precipitation = []  # %
weekly_snow = []  # mm
weekly_cloudcover = []  # %
weekly_severerisk = []  # %
weekly_pressure = []  # hPa
weekly_wind = []  # km/h

for i in range(7):

    today_temperature = []
    today_feels = []
    today_humidity = []
    today_precipitation = []
    today_snow = []
    today_cloudcover = []
    today_severerisk = []
    today_pressure = []
    today_wind = []

    for j in data['days'][i]['hours']:
        today_temperature.append(round((j['temp'] - 32) * (5 / 9), 1))
        today_feels.append(round((j['feelslike'] - 32) * (5 / 9), 1))
        today_humidity.append(j['humidity'])
        today_precipitation.append(j['precipprob'])
        today_snow.append(j['snowdepth'] * 25.4)
        today_cloudcover.append(j['cloudcover'])
        today_severerisk.append(j['severerisk'])
        today_pressure.append(j['pressure'])
        today_wind.append(round(j['windspeed'] * 1.609, 1))

    weekly_temperature.append(today_temperature)
    weekly_feels.append(today_feels)
    weekly_humidity.append(today_humidity)
    weekly_precipitation.append(today_precipitation)
    weekly_snow.append(today_snow)
    weekly_cloudcover.append(today_cloudcover)
    weekly_severerisk.append(today_severerisk)
    weekly_pressure.append(today_pressure)
    weekly_wind.append(today_wind)

weekly_temperature = np.array(weekly_temperature)
weekly_feels = np.array(weekly_feels)
weekly_humidity = np.array(weekly_humidity)
weekly_precipitation = np.array(weekly_precipitation)
weekly_snow = np.array(weekly_snow)
weekly_cloudcover = np.array(weekly_cloudcover)
weekly_severerisk = np.array(weekly_severerisk)
weekly_pressure = np.array(weekly_pressure)
weekly_wind = np.array(weekly_wind)



plt.figure(figsize=(10, 6), dpi=200)
plt.xlabel('день недели')
plt.ylabel('температура, °C')
plt.title(f'Погода в {c.capitalize()}')
plt.xticks([q * 24 for q in range(7)], [f'день {i + 1}' for i in range(7)])
plt.plot(weekly_temperature.reshape(7*24, ), 'o-', label='температура')
plt.plot(weekly_feels.reshape(7*24, ), 'o-', label='ощущается как')
plt.legend()
plt.savefig('temperature.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 6), dpi=200)
plt.xlabel('день недели')
plt.ylabel('влажность, %')
plt.title(f'Погода в {c.capitalize()}')
plt.xticks([q * 24 for q in range(7)], [f'день {i + 1}' for i in range(7)])
plt.plot(weekly_humidity.reshape(7*24, ), 'o-', label='влажность')
plt.plot(weekly_precipitation.reshape(7*24, ), 'o-', label='вероятность осадков')
plt.legend()
plt.savefig('humidity.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 6), dpi=200)
plt.xlabel('день недели')
plt.ylabel('облачность/вероятность, %')
plt.title(f'Погода в {c.capitalize()}')
plt.xticks([q * 24 for q in range(7)], [f'день {i + 1}' for i in range(7)])
plt.plot(weekly_cloudcover.reshape(7*24, ), 'o-', label='облачность')
plt.plot(weekly_severerisk.reshape(7*24, ), 'o-', label='вероятность грозы')
plt.legend()
plt.savefig('cloudcover.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 6), dpi=200)
plt.xlabel('день недели')
plt.ylabel('давление, hPa')
plt.title(f'Погода в {c.capitalize()}')
plt.xticks([q * 24 for q in range(7)], [f'день {i + 1}' for i in range(7)])
plt.plot(weekly_pressure.reshape(7*24, ), 'o-', label='давление')
plt.legend()
plt.savefig('pressure.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 6), dpi=200)
plt.xlabel('день недели')
plt.ylabel('скорость ветра, км/ч')
plt.title(f'Погода в {c.capitalize()}')
plt.xticks([q * 24 for q in range(7)], [f'день {i + 1}' for i in range(7)])
plt.plot(weekly_wind.reshape(7*24, ), 'o-', label='скорость ветра')
plt.legend()
plt.savefig('wind.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(10, 6), dpi=200)
plt.xlabel('день недели')
plt.ylabel('осадки, мм')
plt.title(f'Погода в {c.capitalize()}')
plt.xticks([q * 24 for q in range(7)], [f'день {i + 1}' for i in range(7)])
plt.plot(weekly_snow.reshape(7*24, ), 'o-', label='осадки')
plt.legend()
plt.savefig('snow.png', bbox_inches='tight')
plt.show()
