#-*- coding:UTF-8 -*-
'''
author:Loopher

date:

description: 
使用图像显示数据格式化
可以参看慕课网的机器学习入门-python

'''
import  pandas as pd
import os,sys
# import  matplotlib.
class UI(object):
	def __init__(self,file):
		"""
		:param file: .cvs文件 数据文件
		"""
		self.df = pd.read_csv(file,header=None) #header 通常用于说明文件，如果没有header信息，那么，就设置为none，那么读取真实
	def show_data(self):
		"""
		展示数据
		:return:
		"""
		print (self.df.head(100))

#D:\PythonWork\crawl_baidu\mytensor\csv
if __name__ =="__main__":
	file = sys.path[0]+os.sep+ "iris.csv"
	if not os.path.isfile(file) :
		print  "file is not exits {}".format(file)
	# sys.exit(1)
	ui =  UI(file)
	ui.show_data()