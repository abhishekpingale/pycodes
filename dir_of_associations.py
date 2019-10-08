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
import math
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

def get_main_page_states():
    main_url="https://www.directoryofassociations.com/"
    print("main_url insde get_list_states",main_url)
    #to_do="find table with class table-condensed , create a dict with state name and href value of table descriptor"
    r=requests.get(main_url)
    data=r.text
    soup=BeautifulSoup(data,"lxml")
    table = soup.find('table', {'class': 'table-condensed'})
    rows = table.findAll('tr')
    print("this is rows",rows)
    print("length of rows",len(rows))
    for tr in rows:
        cols = tr.findAll('td')
        print("len(cols)",len(cols))
        for i in range(len(cols)):
            link = cols[i].find('a').get('href')
            state_name = cols[i].text
            print(link)
            print(state_name)
    #table_tag_rows=soup.find("table",class_="table-condensed").find("tbody").find_all("tr")
    #print("table-condensed is ",table_tag)
def get_page_urls_from_main_page():
    state_page_url="https://www.directoryofassociations.com/browse.asp?s=AL"
    browse_url_2="https://www.directoryofassociations.com/browse.asp?dp=2&n=&s=AL&c=&z=&t1=&g=&m="
    browse_url_3="https://www.directoryofassociations.com/browse.asp?dp=3&n=&s=AL&c=&z=&t1=&g=&m="


def fetch_listing_url():
    browse_url_2="https://www.directoryofassociations.com/browse.asp?dp=2&n=&s=AL&c=&z=&t1=&g=&m="
    browse_url_1st="https://www.directoryofassociations.com/browse.asp?dp="
    browse_url_2nd="&n=&s=AL&c=&z=&t1=&g=&m="
    
    state_page_url="https://www.directoryofassociations.com/browse.asp?s=AL"
    #to_do="find table with class table-striped, for every tr tag , find the 2nd td tag href value, div with class col-md-10 has number of listing value, every page has 20 listings"
    r=requests.get(state_page_url)
    data=r.text
    soup=BeautifulSoup(data,"lxml")
    number_of_listings=int(soup.find('div',{'class':'col-md-10'}).h2.strong.text)
    print("below is number",number_of_listings)
    url_index_range=int(math.ceil(number_of_listings/20))
    print("url_index_range :",url_index_range)
    for j in range(1,url_index_range+1):
        print(browse_url_1st+str(j)+browse_url_2nd)
    table = soup.find('table', {'class': 'table-striped'})
    rows = table.findAll('tr')
    print("this is rows",rows)
    print("length of rows",len(rows))
    for tr in rows:
        cols = tr.findAll('td')
        print("inside loop",cols[1].find('a').get('href'))
        print("inside loop",cols[1].text)

def get_page_details(dir_test_url):

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

#get_page_details(dir_test_url)
#get_main_page_states()
fetch_listing_url()
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