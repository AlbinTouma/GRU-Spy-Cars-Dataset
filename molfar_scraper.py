from datetime import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import re


def scrape_data():
    r = requests.get("https://molfar.com/en/gru")
    html = BeautifulSoup(r.text, 'html.parser')
    table = html.find('div', class_='itable')
    name: list = [i.get_text(" ", strip=True) for i in table.find_all('div', class_='itable__row-col gru-cooperators__col--name')]
    address: list[str, int] = [i.get_text(strip=True) for i in table.find_all('div', class_='itable__row-col gru-cooperators__col--address')]
    car: list[str] = [i.get_text(".", strip=True) for i in table.find_all('div', class_='itable__row-col gru-cooperators__col--car')]
    unit: list[str] = [i.get_text(".", strip=True) for i in table.find_all('div', class_='itable__row-col gru-cooperators__col--work')]

    with open('gru.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        header = ['name', 'address', 'car', 'unit']
        writer.writerow(header)
        for n, a, c, u in zip(name, address, car, unit):
            writer.writerow([n, a, c, u])

scrape_data()
