# 第一种方式：分析接口

import requests
from lxml import etree
import time

def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
        'Referer' : 'https://www.lagou.com/jobs/list_Python?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=',
        'Cookie' : '_ga=GA1.2.2034651801.1549981507; user_trace_token=20190212222507-fedffcca-2ed1-11e9-b334-525400f775ce; LGUID=20190212222507-fee0017c-2ed1-11e9-b334-525400f775ce; _gid=GA1.2.518631166.1549981507; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAAADEAAFI6DD3294CB2193F6C00F216F7E8380C60; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1549981507,1550041754; TG-TRACK-CODE=index_search; _gat=1; LGSID=20190213202918-fb935f58-2f8a-11e9-b77b-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3Fcity%3D%25E5%25B9%25BF%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_Python%3Fcity%3D%25E5%25B9%25BF%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; SEARCH_ID=69f59b67b70e4f1d887edbcaeefbe6ae; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1550060962; LGRID=20190213202922-fe097ae4-2f8a-11e9-b77b-525400f775ce',
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
    data = {
        'first': "false",
        'pn': 1,
        'kd': 'Python'
    }
    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url,headers=headers,data=data)
        # json：如果返回的是json数据，那么这个方法会自动的load成字典
        print(response.json())
        time.sleep(1)

def main():
    request_list_page()

if __name__ == '__main__':
    main()