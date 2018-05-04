import threading
from bs4 import BeautifulSoup
import requests
import time


class ScraperThread(threading.Thread):

    def __init__(self, url, subscriber):
        threading.Thread.__init__(self)
        self.url = url
        self.subscriber = subscriber
        self.new_einsotz = ""

    def run(self):
        while True:
            data = self.get_data()
            if not data['nummer'] == self.new_einsotz:
                self.new_einsotz = data['nummer']
                self.subscriber.update(data)
            time.sleep(30)

    def get_data(self):
        page = requests.get(self.url).content
        soup = BeautifulSoup(page, "lxml")
        row = soup.find_all('td')[:6]
        data = {'nummer': row[0].text, 'feuerwehr': row[1].text, 'bezirk': row[2].text, 'art': row[3].text, 'alarmstufe': row[4].text, 'zeit': row[5].text}
        print(data)
        return data

