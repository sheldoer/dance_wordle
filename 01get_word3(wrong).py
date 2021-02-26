import requests
import pandas as pd
import re
import time
import random
from concurrent.futures import ThreadPoolExecutor
import datetime
from fake_useragent import UserAgent

# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')
start_time = datetime.datetime.now()

def  Grab_barrage(date):
    # 伪装请求头
    headers = {
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "accept-encoding": "gzip",
        "origin": "https://www.bilibili.com",
        "referer": "https://www.bilibili.com/video/BV1rD4y1Q7jc?from=search&seid=10634574434789745619",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "cookie": "finger=158939783; _uuid=F614D475-1000-98CB-AE2B-030E8A99233620064infoc; buvid3=85688788-2FD7-4707-8AD2-EE8CC7EE4C3B143108infoc; sid=6dthda6c; DedeUserID=383307308; DedeUserID__ckMd5=be1f10fb7bcaa330; SESSDATA=f5f80249%2C1614929656%2C1049b*91; bili_jct=4cf3d93ff38ae412d8273d1bc6f57072; blackside_state=1; rpdid=|(J|YYl~Rl|l0J'ulmmR~Jmum; CURRENT_FNVAL=80; LIVE_BUVID=AUTO8115999665925670; LIVE_PLAYER_TYPE=2; CURRENT_QUALITY=80; bp_video_offset_383307308=487137656033947369; finger=158939783; PVID=3; bp_t_offset_383307308=488982078192148941"
    }
    # 构造url访问   需要用到的参数  爬取指定日期的弹幕
    params = {
        'type': 1,
        'oid': '206344228',
        'date': date
    }
    # 发送请求  获取响应
    response = requests.get(url, params=params, headers=headers)
    # print(response.encoding)   重新设置编码
    response.encoding = 'utf-8'
    print(response.text)
    # 正则匹配提取数据  转成集合去除重复弹幕
    comment = set(re.findall('<d p=".*?">(.*?)</d>', response.text))
    # 将每条弹幕数据写入txt
    #playerAuxiliary > div > div.player-auxiliary-collapse.bui.bui-collapse > div > div.bui-collapse-body > div > div.player-auxiliary-filter-wrap.player-auxiliary-danmaku > div.player-auxiliary-danmaku-wrap > div.player-auxiliary-danmaku-contaner.player-auxiliary-bscrollbar > ul > li.danmaku-info-row.bpui-selected > span.danmaku-info-danmaku
    with open('bullet.txt', 'a+') as f:
        for con in comment:
            f.write(con + '\n')
            print(con)
    time.sleep(random.randint(1, 3))   # 休眠
def main():
    # 开多线程爬取   提高爬取效率
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(Grab_barrage, date_list)
    # 计算所用时间
    delta = (datetime.datetime.now() - start_time).total_seconds()
    print(f'用时：{delta}s  -----------> 弹幕数据成功保存到本地txt')
if __name__ == '__main__':
    # 目标url
    url = "https://api.bilibili.com/x/v2/dm/history"
    start = '20201201'
    end = '20210207'
    # 生成时间序列
    date_list = [x for x in pd.date_range(start, end).strftime('%Y-%m-%d')]
    print(date_list)
    count = 0
    # 调用主函数
    main()
