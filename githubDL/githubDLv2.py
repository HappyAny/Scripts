#!/usr/bin/env python
# coding: utf-8

# In[2]:


#coding=utf-8
import urllib.request as request
import xml
from bs4 import BeautifulSoup
import os


def urllib_download(pic_url, file_path):
    from urllib.request import urlretrieve
    urlretrieve(pic_url, file_path)

def get_repo_url(soup):
    repo_url=[]
    name=[]
    for i in soup.find_all('a',itemprop='name codeRepository'):
        repo_url.append('https://github.com'+i['href']+'/archive/master.zip')
        name.append(i['href'][1:].replace("/", "_"))
    return repo_url,name

def get_one_page(url):
    global opener
    origin_bytes = opener.open( url ).read()
    origin_string = origin_bytes.decode( 'utf-8' )
    soup = BeautifulSoup(origin_string, "lxml")
    return soup

def get_repo_zip(file_path,repo_url,name):
    print ("Downloading repo="+name)
    urllib_download(repo_url,file_path+name+'.png')
    print ("OK...repo="+name)
    return
    
def main():
    url = 'https://github.com/microsoft'
    file_path='./github/'
    os.makedirs(file_path, exist_ok=True)
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    global opener
    opener = request.build_opener()
    opener.addheaders = [ headers ]
    soup=get_one_page(url)
    [repo_url,name]=get_repo_url(soup)
    print(name)
    print(len(name))
    rcount=0
    ecount=0
    for i in range(len(name)):
        try:
            #get_repo_zip(file_path,repo_url[i],name[i])
            rcount=rcount+1
        except:
            #print('Error for '+name)
            ecount=ecount+1
    count=rcount+ecount
    #print ('Program Over.共下载'+str(count)+'个项目,'+str(rcount)+'个成功,'+str(ecount)+'个失败。')
main()


# In[ ]:




