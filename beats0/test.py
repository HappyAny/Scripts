import os
import json

#检测下载是否完全

def LoadJson(file):
    f=open(str(file),encoding='utf-8')
    url_json=json.load(f)
    url_list=url_json['pics']
    f.close()
    return url_list

def main():
    fileList = os.listdir('imageR')
    list1=[]
    list2=[]
    for i in fileList:
        i=str(i).replace(".jpg",'',9)
        list1.append(i)
    url_list=LoadJson('r.json')
    for i in url_list:
        i=str(i).replace("/",'',9)
        list2.append(i)
    print (list1)
    print (list2)
    print (list(set(list1).difference(set(list2))))
    print (list(set(list1).intersection(set(list2))))
    print (list(set(list1).union(set(list2))))

main()
