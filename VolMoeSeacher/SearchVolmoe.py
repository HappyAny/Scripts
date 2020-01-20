#!/usr/bin/env python
# coding: utf-8

# In[13]:


#coding=utf-8
import urllib.request as request
import xml
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import json
import progressbar
import time
#id_new='518044'/'504560'

def urllib_download(pic_url, file_path):
    urlretrieve(pic_url, file_path)

def get_one_page(url):
    global opener
    origin_bytes = opener.open( url ).read()
    origin_string = origin_bytes.decode( 'utf-8' )
    soup = BeautifulSoup(origin_string, "lxml")
    return soup

def get_infon(soup):
    info=soup.find_all('td',colspan="1")
    infoinit=str(info[1]).find('/')
    infoend=str(info[1]).find(' 頁')
    info=str(info[1])[infoinit+2:infoend]
    return int(info)

def get_info(soup):
    information=[]
    info=soup.find_all('tr',class_="listbg")
    for row in info:
        inforow=row.find_all('td')
        for i in inforow:
            infor={}
            inform=i.find_all('a')[1]['href']
            inforn=i.find_all('a')[1].string
            inforl=i.find_all('font')[0].string
            inforo=i.find_all('font')[1].string
            inforp=i.find_all('img')[0]['src']
            inforqindex=str(i).find("<br/>")
            inforqq=str(i)[inforqindex+5:].find("<br/>")
            inforqqq=str(i)[inforqindex+5:][inforqq+7:].find("<br/>")
            inforq=str(i)[inforqindex+inforqq+12:inforqindex+inforqq+10+inforqqq]
            infor['漫画地址']=inform
            infor['漫画标题']=inforn
            infor['最近更新']=inforl
            infor['更新日期']=inforo
            infor['漫画封面']=inforp
            infor['漫画作者']=inforq
            information.append(infor)
    return information

def main():
    widgets = ['Progress: ',progressbar.Percentage(), ' ', progressbar.Bar('#'),' ', progressbar.Timer(),  
           ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]  
    #widgets = [
     #   'Searching: ',
      #  '[', progressbar.AnimatedMarker(), ']',
       # ' ',
        #progressbar.Timer()
    #]
    bar = progressbar.ProgressBar(
        widgets=widgets, maxval=100).start()
    #file_path='./image/'
    #os.makedirs(file_path, exist_ok=True)
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    global opener
    opener = request.build_opener()
    opener.addheaders = [ headers ]
    url='https://volmoe.com/list/all,all,all,sortpoint,all,all/'
    soup=get_one_page(url)
    m=get_infon(soup)+1
    manga=[]
    for n in range(1,m):
        #url='https://yande.re/post?page='+str(n)+'&tags=dakimakura'
        url='https://volmoe.com/list/all,all,all,sortpoint,all,all/'+str(n)+'.htm'
        soup=get_one_page(url)
        #print(soup)
        info=get_info(soup)
        manga.append(info)
        bar.update(int(n/m*100))
        #print('完成对第'+str(n)+'页的检索。')
    bar.finish()
    fw = open('volmoe_'+time.asctime( time.localtime(time.time()) ).replace(' ','_')+'.json', 'w', encoding='utf-8')
    dic_json = json.dumps(manga,ensure_ascii=False,indent=4)  #字典转成json，字典转成字符串
    fw.write(dic_json)
    fw.close()
    print ('Program Over.')

main()


# In[14]:


import os
import json

def get_file_list(file_path,keyword):
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        files=[]
        for i in dir_list:
            if keyword in i:
                files.append(i)
        return files
    
    
file_path=os.getcwd()
file=get_file_list(file_path,'.json')
f1=open(file[-1],encoding='utf-8')
content1=f1.read()
comp1=json.loads(content1)
f2=open(file[-2],encoding='utf-8')
content2=f2.read()
comp2=json.loads(content2)
f1.close()
f2.close()
com1=[]
com2=[]
n=0
for i in comp1:
    for j in i:
        com1.append(str(j["漫画标题"])+'_'+str(j["最近更新"])+'_'+str(j["更新日期"]))
        n=n+1
print('最新'+str(n)+'部')
n=0
for i in comp2:
    for j in i:
        com2.append(str(j["漫画标题"])+'_'+str(j["最近更新"])+'_'+str(j["更新日期"]))
        n=n+1
print('原先'+str(n)+'部')
print (list(set(com1).difference(set(com2))))


# In[ ]:




