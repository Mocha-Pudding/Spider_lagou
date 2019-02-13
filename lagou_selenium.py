# 第二种方式：Selenium + Chromedriver来模拟请求去爬取

from selenium import webdriver
from lxml import etree
import re
import time

class LagouSpider(object):
    driver_path = r"G:\ProgramApp\chromedriver\chromedriver.exe"
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []

    # run方法，爬虫的入口
    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source
        self.parse_list_page(source)

    # parse_list_page()方法：用来解析列表页的页面
    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    # request_detail_page()方法：请求详情页面
    def request_detail_page(self,url):
        self.driver.get(url)
        source = self.driver.page_source
        self.parse_detail_page(source)

    # parse_detail_page()方法：解析详情页面
    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spans[0].xpath('.//text()')[0].strip()
        city = job_request_spans[1].xpath('.//text()')[0].strip()
        city = re.sub(r"[\s/]", "", city)  # 正则表达式
        work_years = job_request_spans[2].xpath('.//text()')[0].strip()
        work_years = re.sub(r"[\s/]", "", work_years)  # 正则表达式
        education = job_request_spans[3].xpath('.//text()')[0].strip()
        education = re.sub(r"[\s/]", "", education)  # 正则表达式
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()

        # 保存职位信息到字典里
        position = {
            'name' : position_name,
            'salary' : salary,
            'city' : city,
            'workyears' : work_years,
            'education' : education,
            'desc' : desc
        }
        self.positions.append(position)
        print(position)
        print('='*60)

if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()