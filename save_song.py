import os


class SaveSong:
    def __init__(self, name, song):
        self.song_name = name
        self.song_content = song
        self.path = '/Users/thesky/Downloads/hot_top200/'

    def save(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        with open(self.path + self.song_name + '.m4a', 'wb') as f:
            f.write(self.song_content)

    def run(self):
        self.save()
        print(self.song_name + 'ok')
