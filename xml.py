import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
items = root.find('channel').findall('item')
result = []
for item in items:
    for tag in ['pubDate', 'title']:
        result.append({tag: item.find(tag).text})
with open('news.json', 'w', encoding='utf8') as f:
    json.dump(result, f)
