# 第一种方式：分析接口

import requests
from lxml import etree
import time
import re

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Referer' : 'https://www.lagou.com/jobs/list_Python?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
    'Cookie' : '_ga=GA1.2.2034651801.1549981507; user_trace_token=20190212222507-fedffcca-2ed1-11e9-b334-525400f775ce; LGUID=20190212222507-fee0017c-2ed1-11e9-b334-525400f775ce; _gid=GA1.2.518631166.1549981507; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAAADEAAFI73B22E3041CBE3BDAB9F2B6875633815; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549981507,1550041754,1550062636,1550063906; LGSID=20190213221126-4061853a-2f99-11e9-b799-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; X_MIDDLE_TOKEN=b90589954ab23bde05ec07796d6393c0; TG-TRACK-CODE=index_search; SEARCH_ID=01e82a4789484ca095a1c735a5116889; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550068409; LGRID=20190213223329-5484ab4d-2f9c-11e9-818c-5254005c3644',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    # 'Host' : 'www.lagou.com',
    # 'Origin' : 'https://www.lagou.com',
    # 'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Content-Length' : '25',
    # 'Connection' : 'keep-alive',
    # 'Accept' : 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding' : 'gzip, deflate, br',
    # 'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
}

def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
    data = {
        'first': "false",
        'pn': 1,
        'kd': 'Python'
    }
    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url,headers=headers,data=data)
        # json：如果返回的是json数据，那么这个方法会自动的load成字典
        # print(response.json())
        result = response.json()
        print('=============>>', result)
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionId
            parse_position_detail(position_url)
            break
        break

def parse_position_detail(url):
    response = requests.get(url,headers=headers)
    # print(response.text)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath("//span[@class='name']/text()")[0]
    # print('------->>>', position_name)
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip()
    city = job_request_spans[1].xpath('.//text()')[0].strip()
    city = re.sub(r"[\s/]","",city)    #正则表达式
    work_years = job_request_spans[2].xpath('.//text()')[0].strip()
    work_years = re.sub(r"[\s/]","",work_years)    #正则表达式
    education = job_request_spans[3].xpath('.//text()')[0].strip()
    education = re.sub(r"[\s/]","",education)    #正则表达式
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()   #把职位详情组合成字符串

def main():
    request_list_page()

if __name__ == '__main__':
    main()