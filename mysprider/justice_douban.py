import requests
from lxml import etree
import pandas as pd
import numpy as np


url = 'https://movie.douban.com/subject/2158490/comments?status=P'
r = requests.get(url,timeout = 5).text
s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/text()')
df = pd.DataFrame(file)
df.to_excel('justice.xlsx')