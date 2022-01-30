import json
import random
import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import codecs


def get_random():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    string = ''
    for i in range(16):
        num = random.random() * len(chars)
        num = math.floor(num)
        string += chars[num]
    return string


def b(d, g):
    data = pad(d.encode('utf-8'), 16)
    aes = AES.new(key=g.encode('utf-8'), mode=AES.MODE_CBC, iv='0102030405060708'.encode('utf-8'))
    text = aes.encrypt(data)
    text = base64.b64encode(text)
    return text.decode('utf-8')


class Parse:
    def __init__(self, _id):
        self.e = "010001"
        self.f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa7" \
                 "6d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46be" \
                 "e255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7 "
        self.g = "0CoJUm6Qyw8W8jud"
        self.i7b = {
            'csrf_token': "",
            'encodeType': "aac",
            'ids': f"[{_id}]",
            'level': "standard"
        }
        self.d = json.dumps(self.i7b)
        self.i = get_random()

    def get_enctext(self):
        first_enctext = b(self.d, self.g)
        second_enctext = b(first_enctext, self.i)
        return second_enctext

    def get_encseckey(self):
        data = self.i[::-1]
        rs = int(codecs.encode(data.encode('utf-8'), 'hex_codec'), 16) ** int(self.e, 16) % int(
            self.f, 16)
        return format(rs, 'x').zfill(256)

    def run(self):
        return self.get_enctext(), self.get_encseckey()


if __name__ == '__main__':
    P = Parse('1808492017')
    params, encSecKey = P.run()
    print(params)
    print(encSecKey)
