# url输出器 输出我们爬到的数据到网页中
class UrlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        fout = open("result.html", "w", encoding="utf-8")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<a>")

        for data in self.datas:
            fout.write('<a href = "%s">%s</a>' % (data['url'], data['title']))
            fout.write('<p>%s</p>' % data['summary'])

        fout.write("</a>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
