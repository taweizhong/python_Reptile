import hot_top
import parse_js
import get_url
import save_song
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

List = hot_top.HotSong()
song_list = List.run()


def run(dic):
    for k, v in dic.items():
        name = k
        song_id = v.split('=')[1]
        P = parse_js.Parse(song_id)
        params, encSecKey = P.run()

        Song = get_url.Song(params, encSecKey)
        song = Song.run()

        S = save_song.SaveSong(name, song)
        S.run()


with ThreadPoolExecutor(20) as t:
    for i in song_list:
        t.submit(run, i)
print('完成')
