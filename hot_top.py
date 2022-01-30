import requests
from bs4 import BeautifulSoup


class HotSong:
    def __init__(self):
        self.url = 'https://music.163.com/discover/toplist?id=3778678'

    def get_song_href(self):
        resp = requests.get(self.url)
        bs = BeautifulSoup(resp.text, "html.parser")
        song_ul = bs.findAll('ul', class_="f-hide")
        song_ul = song_ul[0]
        song_lis = []

        for i in song_ul:
            song_lis.append({i.a.text: i.a['href']})
        return song_lis

    def run(self):
        print('hot song list ok')
        return self.get_song_href()


if __name__ == '__main__':
    s = HotSong()
    song_list = s.run()
    print(song_list)
