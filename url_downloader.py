import string
from urllib import request
from urllib.parse import quote

# url下载器 利用urllib库对url网页进行下载
class UrlDownlader(object):

    def downlaod(self, new_url):
        if new_url is not None:
            url_ = quote(new_url, safe=string.printable)
            res = request.urlopen(url_)

            if res.getcode() != 200:
                return None

            return res.read()

