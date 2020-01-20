#!/usr/bin/env python
# coding: utf-8

# In[13]:


import json
import os
from urllib.request import urlretrieve

def LoadJson(file):
    f=open(str(file),encoding='utf-8')
    url_json=json.load(f)
    url_list=url_json['pics']
    f.close()
    return url_list

def GetUrl(sand1,sUrl,sand2):
    url_list=[]
    for i in sUrl:
        url=sand1+i+sand2
        url_list.append(url)
    return url_list

def GetPic(urls,OutFile,name):
    n=0
    for url in urls:
        print ("Downloading Picture...ID="+name[n])
        urlretrieve(url,OutFile+name[n].replace('/','')+'.jpg')
        print ("OK...ID="+name[n])
        n=n+1
    return n
    
def main(file):
    OutFile='./imageR/'
    os.makedirs(OutFile, exist_ok=True)
    sUrl=LoadJson(file)
    urls=GetUrl('https://steamuserimages-a.akamaihd.net/ugc/',sUrl,'')
    n=GetPic(urls,OutFile,sUrl)
    return n

print(main("r.json"))


# In[ ]:




