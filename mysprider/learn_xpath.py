import requests
from lxml import etree
import pandas as pd
import numpy as np

url = 'http://book.douban.com/subject/1084336/comments/'
r = requests.get(url,timeout = 5).text
# print(r)

s = etree.HTML(r)
print(s.xpath('//div[@class="comment"]/p/text()'))
file = s.xpath('//div[@class="comment"]/p/text()')
#print(s.xpath('//*[@id="comments"]/ul/li[1]/div[2]/p/text()'))
#print(s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()'))

df = pd.DataFrame(file)
df.to_excel('pinglun.xlsx')


