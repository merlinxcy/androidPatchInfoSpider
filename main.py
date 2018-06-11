#! coding:utf-8

import os
import json
import argparse
import datetime
import platform


def search_date(startdate, enddate):
    a = open('1.json')
    result = json.load(a)
    startdate = str(startdate).split('-')
    enddate = str(enddate).split('-')
    startdate = datetime.date(int(startdate[0]), int(startdate[1]), int(startdate[2]))
    enddate = datetime.date(int(enddate[0]), int(enddate[1]), int(enddate[2]))
    for i in result:
        patch_date = i['patch_date'].split('-')
        patch_date = datetime.date(int(patch_date[0]), int(patch_date[1]), int(patch_date[2]))
        if patch_date >= startdate and patch_date <= enddate:
            print i['cve_id']


sysstr = platform.system()
if sysstr == "Windows":
    system = 1
elif sysstr == "Linux":
    system = 2
else:
    system = -1

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="init the requirements", action='store_true')
parser.add_argument("-s", help="start the spider", action='store_true')
parser.add_argument("--cveid",help="search cveid", action="store")
parser.add_argument("--startdate", help="use date(Eg:1990-01-01) to search cve", action="store")
parser.add_argument("--enddate", help="use date(Eg:1990-01-01) to search cve", action="store")
args = parser.parse_args()
sysstr = platform.system()

if args.i:
    try:
        import scrapy
    except:
        if system == 1:
            os.system("python -m pip install scrapy -i https://pypi.douban.com/simple")
        else:
            os.system("pip install scrapy -i https://pypi.douban.com/simple")
elif args.s:
    os.remove('1.json')
    os.system("scrapy crawl android -o 1.json")
elif args.cveid:
    pass
elif args.startdate and args.enddate:
    search_date(args.startdate, args.enddate)