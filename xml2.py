import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def main():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    items = root.find('channel').findall('item')
    select(items)


def select(items):
    result = []
    for item in items:
        data = {}
        for i in item.iter():
            if i != item:
                data[i.tag] = i.text
        result.append(data)
    with open('news2.json', 'w', encoding='utf8') as f:
        json.dump(result, f)

