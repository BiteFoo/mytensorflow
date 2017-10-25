#-*- coding:UTF-8 -*-
'''
author:Loopher

date:

description: 
需要添加访问的代理头，否则不能获取到正确的Html页面
'''
import urllib
import  httplib
import json
import os
import  sys
imgs = sys.path[0]+os.sep+'imgs'
baidu_img_url ='image.baidu.com'
url_item ='/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&cg=girl&rn=60&pn='+str(60) #'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1508907635540_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=3&word=%E7%BE%8E%E5%A5%B3&f=3&oq=mein&rsp=0' #'http://www.baidu.com'
def gethtml():
	'''
	添加header 作为代理
	:return:
	'''
	conn = httplib.HTTPConnection(baidu_img_url)
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
	           'Content-type': 'test/html'}
	conn.request('GET',url_item,headers=headers)
	respose_code =conn.getresponse()
	html =respose_code.read()
	return html
def parse(html_doc):
	print  (type(html_doc))
	if html_doc is None:
		return
	data = unicode(html_doc,errors='ignore')
	decode = json.loads(data)  # json.load(data) 少了s会造成不能类型错误
	dowload_img(decode_data=decode['imgs'])
def dowload_img(decode_data):
	print ("img_length = {}".format(decode_data.__len__()))
	count =0
	for item in decode_data:
		url = item['objURL'] #读取imag url
		print ("img_url = {} , count = {}".format(url,count))
		count+=1
		name =  url[url.rfind('/')+1:]
		print ('name = {} '.format(name))
		img_name = imgs+os.sep+name
		try:
			urllib.urlretrieve(url, img_name)
		except Exception as e:
			#出现不能访问的Url,那么跳过当前
			print  ("write img exception {}".format(e))
			continue
def init_imgs_dir():
	if not os.path.isdir(imgs):
		os.makedirs(imgs)
if __name__ =='__main__':
	init_imgs_dir()
	html_doc = gethtml()
	parse(html_doc)


