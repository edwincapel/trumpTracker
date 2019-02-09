import feedparser
import json
import schedule
import time
import os

def job():
    NEWS_SOURCE = ['https://www.aljazeera.com/xml/rss/all.xml','http://www.wsj.com/xml/rss/3_7085.xml']

    if os.path.getsize('articles.json') > 0:
        with open('articles.json') as json_file:  
            data = json.load(json_file)
            for source in NEWS_SOURCE:
                d = feedparser.parse(source)
                for entry in d.entries:
                    if 'trump' in entry.summary.lower() and entry.title.lower() not in str(data).lower():
                        data['article'].append(entry)
    else:
        data = {}
        data['article'] = []
        for source in NEWS_SOURCE:
            d = feedparser.parse(source)
            for entry in d.entries:
                if 'trump' in entry.summary.lower():
                    data['article'].append(entry)

    with open("articles.json", "w") as myfile:
        json.dump(data, myfile)

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)