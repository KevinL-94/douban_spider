# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    def __init__(self):
        pass

    def parse_html_info(self, html_doc):
        if html_doc is None:
            print("HTML document is unavailable")
            return None

        soup = BeautifulSoup(html_doc, "html.parser")

        movies_li = soup.find_all('li', attrs={"data-category": "nowplaying"})
        movies_list = []
        for li in movies_li:
            movie_info = {}
            movie_info['影片名'] = li['data-title']
            movie_info['评分'] = li['data-score']
            link = li.find('a', href=re.compile(r"/subject/\d+/"))
            movie_info['链接'] = link['href']
            movies_list.append(movie_info)

        return movies_list
