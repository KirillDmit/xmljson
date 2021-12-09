import datetime
from itertools import groupby
from urllib.request import urlopen
from json import loads


def get_date(x):
    return datetime.datetime.strptime(x['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0' \
      '%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
stat = {}
data = loads(urlopen(url).read().decode('utf8'))
group = groupby(data['query']['pages']['192203']['revisions'], get_date)
for date, changes in group:
    stat.update({date: len(list(changes))})

for date in stat:
    print(date, stat[date])

#дата смерти Жан-Поля Бельмондо - 2021-09-06
#Такой метрикой пользоваться можно,
# но не факт, что всплеск правок вызван именно уходом человека из жизни

