# -*- coding:utf-8 -*-

import requests
import pandas as pd
import time

headers = {
    'authorization':'Bearer 2|1:0|10:1510994105|4:z_c0|92:Mi4xb1RxYUJRQUFBQUFBY0VLWG5xU3pEQ2NBQUFDRUFsVk51WDAzV2dEcHRkLXZPS1BNRkJDV3BCcTRYdmRMVy1kQ2FB|eeadf92ca3f962e1ec2d8bde539e5c4832a95994c93a8989e671f7b96b166501',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

user_data = []

def get_user_data(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i * 20)
        #url = 'https://www.zhihu.com/people/excited-vczh/following?page={}'.format(i*20)
        response = requests.get(url,headers = headers).json()['data']
        user_data.extend(response)
        print('正在爬取第%s页' % str(i+1))
        time.sleep(10)

if __name__ == '__main__':
    get_user_data(20)
    df = pd.DataFrame.from_dict(user_data)
    df.to_excel('user1.xlsx')
