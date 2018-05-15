#!/usr/bin/env python3
import argparse
import sys
from robobrowser import RoboBrowser
parser = argparse.ArgumentParser()
parser.add_argument("t", help="topic number",
type=int)
args = parser.parse_args()
theme_id = args.t

fconf = open('config.txt', 'r')
tconf = fconf.read()
fconf.close()
conf_list = tconf.split('\n')
login = conf_list[0]
password = conf_list[1]

ftab = open('upload.csv', 'r')
tables = ftab.read()
ftab.close()
tables_lines = tables.split('fFx')
line_count = len(tables_lines)-1

product_name = [] #0
smallpic     = [] #1
bigpic       = [] #2
descr        = [] #3
sku          = [] #4
color_size   = [] #5
price        = [] #6

for x in range(0, line_count):
    temp_list = tables_lines[x].split(';')
    #for val in temp_list:
    # print(len(val))
    product_name.append(temp_list[0])
    smallpic.append(temp_list[1])
    bigpic.append(temp_list[2])
    descr.append(temp_list[3])
    sku.append(temp_list[4])
    color_size.append(temp_list[5])
    price.append(temp_list[6])


login_url = 'https://ogromno.com/index.php?showuser=1'
theme_url = 'https://ogromno.com/index.php?act=zakup&CODE=00&tid='+str(theme_id)

browser = RoboBrowser(history=True)
browser.open(login_url)
form = browser.get_form(action='https://ogromno.com/index.php')
form['UserName'].value = login
form['PassWord'].value = password
browser.submit_form(form)

for x in range(0, line_count):
    browser.open(theme_url)
    form = browser.get_form(action='/index.php')
    #form = browser.get_form(id='prodpost')
    #form = browser.get_form(class_='prodpost')
    #browser.get_forms()[1]
    form['name'].value       = product_name[x].encode('cp1251')
    form['small_img'].value  = smallpic[x]
    form['big_img'].value    = bigpic[x]
    form['short_desc'].value = descr[x].encode('cp1251')
    form['articul0'].value   = sku[x].encode('cp1251')
    form['razmer0'].value    = color_size[x].encode('cp1251')
    form['cena0'].value      = str(price[x]).encode('cp1251')
    browser.submit_form(form)

