import requests


class Song:
    def __init__(self, encText, encSecKey):
        self.url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
        self.data = {
            'params': encText,
            'encSecKey': encSecKey
        }

    def get_song_href(self):
        resp = requests.post(url=self.url, data=self.data)
        song = resp.json()
        return song['data'][0]['url']

    def get_song(self, href):
        resp = requests.get(url=href)
        return resp.content

    def run(self):
        href = self.get_song_href()
        return self.get_song(href)


if __name__ == '__main__':
    params = 't5uDGEYaEi+HHVKGcjWj2vn/Ex6hFu03onghbPztl+rkeyGvcwQ1kBnXcBE3hkJs+/cS9TSI0adMxqBkAVBIJpwQAV2kCNwsU/f9q9u0iMQdF16Wg3jNEdSTrTgQziFUA+O84cWbnxGfVKPfhF1GmQXCh8vudu03U1uzu7mLiT1qyhZqRgp3yqYvk/bY0aXl'
    encSecKey = '66e9d15f043a891b5ab48e7a9e8908beafaaa160efd2497f2e3585f5f055c5f5f867aa19322e45ee548c638d17036ff6a0ce4ff0fe47959b03f18f66a3e5199903a1bf25e96c826d3e8b4f1265a9c53087740225c2d00dcf21e8897df35ecaa1908e60d5a273d93f5dc89b51dd00c51a7413fd4302212b21ef47ef7ae0a14456'
    Song = Song(params, encSecKey)
    song = Song.run()
    print(song)
