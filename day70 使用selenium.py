'''
import requests

from bs4 import BeautifulSoup


def main():
    resp = requests.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(resp.text, 'lxml')
    for img_tag in soup.select('img[src]'):
        print(img_tag.attrs['src'])


if __name__ == '__main__':
    main()
'''

#运行上面的程序会发现没有任何的输出，因为页面的HTML代码上根本找不到<img>标
# 签。接下来我们使用Selenium来获取到页面上的动态内容，再提取主播图片。

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    driver = webdriver.Chrome()
    driver.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for img_tag in soup.body.select('img[src]'):
        print(img_tag.attrs['src'])


if __name__ == '__main__':
    main()