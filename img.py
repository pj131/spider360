# --*-- Encoding: UTF-8 --*--
import requests
import urllib
import re
import sys
import os
import json

def req_get_json(url) :
    '''requests url , and re findall string , return list'''
    r=requests.get(url)
#    print(url)
#    print(r.content)
    j=json.loads(r.content)
#    print(j['list'])
    return j['list']

#    l=re.findall(r.content,string)
#    print('found ',len(l),' from ',url)
#    return l


def req_get_findall(url,string) :
    '''requests url , and re findall string , return list'''
    r=requests.get(url)
    l=re.findall(r.content,string)
    print('found ',len(l),' from ',url)
    return l

savecount=0
def save_url(filename,url) :
    '''save url as file'''
    if os.path.exists(filename):
        print(filename,'is exist')
        return
    global savecount
    print('save file : ',filename)
    print('url : ',url)
    r=requests.get(url)
    imgfile=open(filename, "wb")
    imgfile.write(r.content)
    imgfile.close()
    savecount = savecount + 1
