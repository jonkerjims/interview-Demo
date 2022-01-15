# -*- coding: utf-8 -*-
import random
import time
from concurrent import futures

import requests
from lxml import html



def plus_times(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    print(url,headers)
    pageObject = requests.get(url,headers=headers)
    tree = html.etree.HTML(pageObject.content)
    xpath = '//*[@id="time"]/text()'
    text = tree.xpath(xpath)
    print(text)


if __name__ == '__main__':
    executor = futures.ThreadPoolExecutor(max_workers=5)

    url = 'http://39.103.157.111:3359/tree/index/{}'

    for i in range(1000, 2000):
        executor.submit(plus_times, url.format(i))
        # time.sleep(random.randint(1,20))


