import re
import urllib.parse
from bs4 import BeautifulSoup

# 利用beautifulSoup来对网页惊醒解析 获取我们需要的数据
class UrlParser(object):

    def parse(self, page_url, page_content):
        if page_url is None or page_url is None:
            return

        soup = BeautifulSoup(page_content, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    # 获取新的urls
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.findAll("a", href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            # Py3中用到的模块名称变为urllib.parse
            new_urls.add(new_full_url)

        return new_urls

    # 获取关心的内容
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node is None:
            return
        res_data['summary'] = summary_node.get_text()

        return res_data
