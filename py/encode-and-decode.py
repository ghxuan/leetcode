import string
import random


class Codec:
    dlu = string.digits + string.ascii_lowercase + string.ascii_uppercase
    # longUrl shortUrl
    l_s_save = s_l_save = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if self.l_s_save.get(longUrl):
            return 'http://tinyurl.com/' + self.l_s_save[longUrl]
        rand_str = ''.join(random.choices(self.dlu, k=6))
        while self.s_l_save.get(rand_str):
            rand_str = ''.join(random.choices(self.dlu, k=6))
        self.l_s_save[longUrl] = rand_str
        self.s_l_save[rand_str] = longUrl
        return 'http://tinyurl.com/' + rand_str

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        short = shortUrl.split('/')[-1]
        if self.s_l_save.get(short):
            return self.s_l_save[short]
        return None


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
res = codec.decode(codec.encode(url))
print(res == url)