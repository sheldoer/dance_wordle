import requests
from bs4 import BeautifulSoup
import pymysql
import re

# css选择器定位标签
def get_informations(html):
    soup = BeautifulSoup(html, "lxml")
    danmu_list=soup.select('div.opened > div:nth-child(8) > span:nth-child(2)')
    danmus=[]
    for each in danmu_list:
        danmu=each.text.strip()
        danmus.append(danmu)
    return danmus
def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        #,'Host': 'movie.douban.com'
    }
    link = 'file:///E:/allcode/python_note/210207ciyun/%E8%88%9E%E8%B9%88%E8%A7%86%E9%A2%91/%E4%B8%8D%E8%A6%81%E5%BF%83%E5%8A%A8%E2%9D%A4%EF%B8%8F%E6%88%91%E8%A6%81%E5%BC%80%E5%A7%8B%E8%A1%A8%E7%99%BD%E4%BA%86%E3%80%90%E6%AC%A3%E5%B0%8F%E8%90%8C%E3%80%91%20(P1.%20%E6%A8%AA%E5%B1%8F%E7%89%88).cmt.xml'
    r = requests.get(link, headers=headers, timeout=10)
    print(get_informations(r.text))
    
if __name__=='__main__':
    main()


