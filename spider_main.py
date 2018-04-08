import url_manager
import url_downloader
import url_outputer
import url_parser


class SpiderMain(object):

    def __init__(self):
        self.url_manager = url_manager.UrlManager()
        self.url_downlader = url_downloader.UrlDownlader()
        self.url_parser = url_parser.UrlParser()
        self.url_outputer = url_outputer.UrlOutputer()


    def start(self, root_url):
        count = 1
        self.url_manager.add_new_url(root_url)
        while self.url_manager.has_new_url():
            new_url = self.url_manager.get_new_url()
            print("new_url %d %s" %(count, new_url))
            url_content = self.url_downlader.downlaod(new_url)
            new_urls, new_data = self.url_parser.parse(new_url, url_content)
            self.url_manager.add_new_urls(new_urls)
            self.url_outputer.collect_data(new_data)

            if count >= 100:
                break
            count += 1

        self.url_outputer.output_html()



if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    baike_spider = SpiderMain()
    baike_spider.start(root_url)
