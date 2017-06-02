# -*- coding: utf-8 -*-
import urllib.request

class HtmlDownloader(object):
    """docstring for ClassName"""
    def __init__(self):
        pass

    def download_html_info(self, url):
        if url is None:
            print("This url is unavaible")
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            print("Response error")
            return

        return response.read()