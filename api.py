import datetime
from itertools import groupby
from urllib.request import urlopen
from json import loads


def get_date(x):
    return datetime.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0' \
      '%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80' \
      '%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87 '
stat = {}
data = loads(urlopen(url).read().decode('utf8'))
group = groupby(data['query']['pages']['183903']['revisions'], get_date)
for date, changes in group:
    stat.update({date: len(list(changes))})
with open('api.txt', 'w', encoding='utf8') as file:
    for date in stat:
        print(date, stat[date], file=file)

#2021-11-28 - день ухода Градского из жизни


