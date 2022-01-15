import json
import time
from concurrent import futures

from lxml import html

import requests

url = 'https://bbs.hupu.com/acg'

headers = {'cookie':'acw_tc=2f624a6e16400832871118794e1b1779e312ad266a4655aaf5f597e3e778ac; csrfToken=q0gNTro2PNPikhinGXpKasUi; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ddc94a4c9a28-0eeb6bf2cbd1158-31346d-2073600-17ddc94a4cabcb%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217ddc94a4c9a28-0eeb6bf2cbd1158-31346d-2073600-17ddc94a4cabcb%22%7D; Hm_lvt_df703c1d2273cc30ba452b4c15b16a0d=1640083269; _HUPUSSOID=0de20d7f-85f5-4e61-a98a-7753ddd0eb1d; smidV2=202112211845451abfc68edeba59658d34622225f785f30033adc0a32558540; _CLT=00376064be821b71351c003dda774e37; u=95675969|6JmO5omRSlIwMjM5Mzg0NDY2|8af6|5e856a5db5b1df06d7e0ad7c55fcdd45|b5b1df06d7e0ad7c|aHVwdV9hOTMzZjhlOTZmNjJmMDQw; ua=23429764; us=e13df5774470b4656e35912e117a30f85190078115be610ec5859e58edb2e9962b8ab7b686dfc480390ef0bdd2c7cb577b64e8271924489de39364acf8eaeaa9; Hm_lvt_4fac77ceccb0cd4ad5ef1be46d740615=1640083588; Hm_lpvt_4fac77ceccb0cd4ad5ef1be46d740615=1640083588; Hm_lvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1640083589; Hm_lpvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1640083589; Hm_lpvt_df703c1d2273cc30ba452b4c15b16a0d=1640083877',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

# 定义一个线程池
executor = futures.ThreadPoolExecutor(max_workers=5)

# 获取详细页url
def acq_details_url(url):
    r = requests.get(url, headers=headers)
    tree = html.etree.HTML(r.content)
    xp = '//*[@id="container"]/div/div[3]/div/div[2]/div[3]/ul/li[*]/div/div[1]/a/@href'
    details_url_list = tree.xpath(xp)
    add = 'https://bbs.hupu.com'
    details_url_list = [add+url for url in details_url_list]
    return details_url_list

def acq_content(del_url):

    r = requests.get(del_url, headers=headers)
    # time.sleep(2)
    tree = html.etree.HTML(r.content.decode('utf-8'))
    title = tree.xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/h1/text()')
    # print(title)
    # print(del_url)
    context = tree.xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div/div/div[4]/div/div[2]/div[1]/div[1]/p/text()')
    comment = tree.xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div[*]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/p/text()')
    content = {
        'title':title,
        'context':context,
        'comment':comment,
    }
    return content

if __name__ == '__main__':
    # 详细页url
    details_url = acq_details_url(url)
    # 详细页内容
    content = []
    # 获取标题、主题内容和第一页的所有回复内容
    for del_url in details_url:
        content.append(executor.submit(acq_content, del_url))

    # print(details_url)
    for con in content:
        # print(con.result())
        with open('./result.txt','a',encoding='utf-8') as f:
            res = con.result()
            res = json.dumps(res,ensure_ascii=False) + '\n'
            print(res)
            f.write(res)

