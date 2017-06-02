# -*- coding: utf-8 -*- 
from douban_spider2 import urls_manager, html_downloader, html_parser, cont_outputer

class SpiderMain(object):
    """docstring for SpiderMain"""
    def __init__(self):
        self.urls = urls_manager.UrlsManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = cont_outputer.ContOutputer()

    def crawl(self, url):
        html_doc = self.downloader.download_html_info(url) 
        cont = self.parser.parse_html_info(html_doc)
        self.outputer.output_html_info(cont)

if __name__ == '__main__':
    url = "https://movie.douban.com/cinema/nowplaying/"
    obj_spider = SpiderMain()
    obj_spider.crawl(url)