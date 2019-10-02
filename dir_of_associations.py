#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: To get the
#
# Author:      Abhishek
# Version:1.1 (folder created for Nifty for a date)
# Created:     16/04/2017
# Copyright:   (c) admin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv,json,sys
from bs4 import BeautifulSoup
from types import *
import requests,os
from datetime import datetime
import logging
from random import choice
from datetime import datetime
from lxml import html

#csv_file_name will be td content with class 'textFontCBold'
print("sys.version_info",sys.version_info)
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler=logging.FileHandler('NSE_logger.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
state_url=["https://www.directoryofassociations.com/browse.asp?s=TX"]
csv_filename="dir_associations_list.csv"
dir_test_url="https://www.directoryofassociations.com/view.asp?di={B1EB94E0-7A4B-433D-857C-A58E20FF32CD}"
r=requests.get(dir_test_url)
data=r.text
soup=BeautifulSoup(data,"lxml")
div_tag=soup.find_all("div", class_="jumbotron")
print("here")
print(div_tag)

print("one")
print(soup.h1)
heading_name=soup.h1.contents

print("heading_name :",heading_name)
website_url=soup.h2.a.contents
print("website_url :",website_url)
#street_value=soup.find_all("itemprop"="street-address")
#abc_var=soup.find_all("item-prop"="street-address")

#print("street_name :",soup.find_all(attrs={"itemprop": "street-address"}))
street_name=soup.find_all(attrs={"itemprop": "street-address"})[0].text
print("street_name :",street_name)
locality_city_name=soup.find_all(attrs={"itemprop": "locality"})[0].text
print("locality_city_name :",locality_city_name)
region_state_name=soup.find_all(attrs={"itemprop": "region"})[0].text
print("region_state_name :",region_state_name)
postalcode_name=soup.find_all(attrs={"itemprop": "postal-code"})[0].text
print("postalcode_name :",postalcode_name)
country_name=soup.find_all(attrs={"itemprop": "country-name"})[0].text
print("country_name :",country_name)
telphone_val=soup.find_all(attrs={"itemprop": "tel"})[0].text
print("telphone_val :",telphone_val)

#print("street_name :",soup.p.span.find_all(itemprop="street-address"))

#my_table=soup('table',{'width':"60%"})[0]
#dir_url="https://www.directoryofassociations.com/view.asp?di="
'''with open(csv_filename,'w'
) as csv_file:
    writer=csv.writer(csv_file,delimiter=' ',dialect=csv.excel)
    writer.writerow(csv_header_row)
    for links in nse_list_to_scrape:
        #scrapper_obj.check_buy_sell_ratio(links)
        string_row=scrapper_obj.buy_sell_price_ratio(links)
        print("string_row :"+string_row)
        #writer=csv.writer(csv_file,delimiter=',',dialect=csv.excel)
        writer.writerow(string_row)
        #logger.info('%s',string_row)
    #scrapper_obj.check_buy_sell_ratio(links)
    #logger.info('asdasd created is :')
'''