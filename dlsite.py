import requests
from lxml import html
from lxml import etree
import os, sys

#f_result=open("dlsite.txt","a")
for i in range(1,4):
    url='https://www.dlsite.com/maniax/works/voice?page='+str(i)+'#search_result_list'
    page=requests.Session().get(url,cookies=cookie)
    tree=html.fromstring(page.text)
    result = tree.xpath('//div[@class="_search_result_container"]//a[@class="work_thumb_inner"]/@herf')
    for res in result:
        print(res)
        #f_result.write(res1+'\n')

#f_result.close()
