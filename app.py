import feedparser
import json
import time
import os

NEWS_SOURCE = ['https://www.aljazeera.com/xml/rss/all.xml','http://www.wsj.com/xml/rss/3_7085.xml']

FILE = 'data/articles.json';
data = None;

if os.path.isfile(FILE) and os.path.getsize(FILE) > 0:
    with open(FILE) as handle:  
        data = json.load(handle)
else:
    data = {}
    data['articles'] = {};

for source in NEWS_SOURCE:
    d = feedparser.parse(source)
    for entry in d.entries:
        if ('trump' in entry.summary.lower() and
            entry.link not in data['articles']):
            data['articles'][entry.link] = entry

with open(FILE, "w") as handle:
    json.dump(data, handle)
