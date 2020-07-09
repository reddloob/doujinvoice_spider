import requests
from lxml import html
from lxml import etree
import os, sys

cookie = {'adultchecked': '1'}{"cookie": "cookie: dlsite_dozen=4; uniqid=0.1yahy3f2tqy; _gcl_au=1.1.1518282186.1590775536; adultchecked=1; _ga=GA1.2.986504353.1590775538; _gaid=986504353.1590775538; adr_id=8VI90GTl1icPxCK86NGIdYykeWNPl4P17r50eFgm9uw2RJKP; _jp_user=1; vendor_design=normal; DL_STAR_ID=10; _gaexp=GAX1.2.Pdl3rKdDTOqJb1ZTgZLaEw.18500.0!PFKWbGe3TuOpy_6M72hnGQ.18501.1; Qs_lvt_328467=1591122786%2C1591129255%2C1591162755%2C1591431274%2C1591431285; Qs_pv_328467=2696389731417653000%2C755940344260245600%2C3924040468800079000%2C4600409025598726000%2C2715163903190604300; locale=zh-cn; _inflow_dlsite_params=%7B%22dlsite_referrer_url%22%3A%22https%3A%2F%2Fwww.dlsite.com%2Findex.html%22%7D; _inflow_params=%7B%22referrer_uri%22%3A%22%22%7D; _inflow_ad_params=%7B%22ad_name%22%3A%22referral%22%7D; uhashjp=15f1a5a058592448a509f4167aa9e24a0669e658; uid_jp=SFT000001513123; last_wishlist_check=0; utm_c=bnlink; DL_SITE_DOMAIN=maniax; DL_PRODUCT_LOG=%2CRJ291628%2CRJ256346%2CRJ278752%2CRJ235333%2CRJ221200%2CRJ258750%2CRJ273917%2CRJ280319%2CRJ287596%2CRJ232664%2CRJ107543%2CRJ114650%2CRJ113852%2CRJ043419%2CRJ290793%2CRJ293192%2CRJ292068%2CRJ292745%2CRJ259207%2CRJ292833%2CRJ279425%2CRJ279368%2CRJ284003%2CRJ288826%2CRJ285565%2CRJ283737%2CRJ284762%2CRJ283087%2CRJ289360%2CRJ264967%2CRJ282879%2CRJ282631%2CRJ282001%2CRJ292031%2CRJ281791%2CRJ290117%2CRJ229029%2CRJ258345%2CRJ292731%2CRJ287333%2CRJ292434%2CRJ290655%2CRJ292174%2CRJ291428%2CRJ270545%2CRJ228996%2CRJ243896%2CRJ257884%2CRJ291841%2CRJ126146; loginchecked=1; dlloginjp=1; eridjp=SFT000001513123; session_state=1338404dac6a6ddd69710f59155c5c179ea8c750a15ada13d84367bab255a3aa.2dkluxh043vosw0wskocc0go0; __DLsite_SID=5p7n1k8m9910kb7bap1r6rn2ba; iom_jp=SFT000001513123"}
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
