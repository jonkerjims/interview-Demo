import time

import requests

from fake_useragent import UserAgent   # 下载：pip install fake-useragent
import requests

# ua = UserAgent()        # 实例化，需要联网但是网站不太稳定-可能耗时会长一些
# headers = {
#     'User-Agent': ua.random    # 伪装
#     }


url = 'http://210.45.176.158/PHOTO_WEB/{}.jpg'


for i in range(21720781, 21720799):
    try:
        # result = requests.get(url.format(i), headers=headers).content
        result = requests.get(url.format(i)).content

        with open('results/{}.jpg'.format(i), 'wb') as f:
            f.write(result)
    except:
        print('没有{}这个人'.format(i))
    time.sleep(1)

