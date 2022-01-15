from concurrent import futures

import requests
from bs4 import BeautifulSoup

headers = {'cookie':'acw_tc=2f624a6e16400832871118794e1b1779e312ad266a4655aaf5f597e3e778ac; csrfToken=q0gNTro2PNPikhinGXpKasUi; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ddc94a4c9a28-0eeb6bf2cbd1158-31346d-2073600-17ddc94a4cabcb%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217ddc94a4c9a28-0eeb6bf2cbd1158-31346d-2073600-17ddc94a4cabcb%22%7D; Hm_lvt_df703c1d2273cc30ba452b4c15b16a0d=1640083269; _HUPUSSOID=0de20d7f-85f5-4e61-a98a-7753ddd0eb1d; smidV2=202112211845451abfc68edeba59658d34622225f785f30033adc0a32558540; _CLT=00376064be821b71351c003dda774e37; u=95675969|6JmO5omRSlIwMjM5Mzg0NDY2|8af6|5e856a5db5b1df06d7e0ad7c55fcdd45|b5b1df06d7e0ad7c|aHVwdV9hOTMzZjhlOTZmNjJmMDQw; ua=23429764; us=e13df5774470b4656e35912e117a30f85190078115be610ec5859e58edb2e9962b8ab7b686dfc480390ef0bdd2c7cb577b64e8271924489de39364acf8eaeaa9; Hm_lvt_4fac77ceccb0cd4ad5ef1be46d740615=1640083588; Hm_lpvt_4fac77ceccb0cd4ad5ef1be46d740615=1640083588; Hm_lvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1640083589; Hm_lpvt_b241fb65ecc2ccf4e7e3b9601c7a50de=1640083589; Hm_lpvt_df703c1d2273cc30ba452b4c15b16a0d=1640083877',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

session = requests.Session()
# 应对反爬，需要更新 headers
session.headers.update(headers)
# 定义一个线程池
executor = futures.ThreadPoolExecutor(max_workers=5)

# 解析列表页，得到内容页链接
def parse_list_page(text):
  soup = BeautifulSoup(text, 'html.parser')
  ul = soup.find('div', class_='bbs-sl-web-post').find('ul')
  urls = []
  prefix = 'https://bbs.hupu.com'
  for li in ul.find_all('li'):
    url = li.div.find('a', class_='p-title').attrs['href']
    url = prefix + url
    urls.append(url)
  return urls


# 解析内容页，得到标题和回复
def parse_content_page(text):
  soup = BeautifulSoup(text, 'html.parser')
  title = soup.find('h1', class_='name').text

  contents = []
  for floor in soup.find_all('div', class_='post-reply-list-container'):
    floor_box = floor.find('div', class_='thread-content-detail')
    if not floor_box:
      return None, None
    content = floor_box.text
    contents.append(content)
  return title, contents


# 爬取列表页，解析出这一页的内容链接
def get_content_urls(list_url):
  res = session.get(list_url)
  content_urls = parse_list_page(res.text)
  return content_urls

# 爬取内容页，解析出标题和回复
def get_content(content_url):
  res = session.get(content_url)
  title, contents = parse_content_page(res.text)
  return title, contents

# 获取内容页链接
fs = []
url = 'https://bbs.hupu.com/acg'
fs.append(executor.submit(get_content_urls, url))
futures.wait(fs)
content_urls = set()
for f in fs:
  for url in f.result():
    content_urls.add(url)
for i in content_urls:
  print(i)
# 爬取内容页
fs = []
for url in content_urls:
  fs.append(executor.submit(get_content, url))
futures.wait(fs)
result = {}
for f in fs:
  title, contents = f.result()
  if title:
    result[title] = contents

print(result.keys())


