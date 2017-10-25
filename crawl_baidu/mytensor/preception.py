#-*- coding:UTF-8 -*-
'''
author:Loopher

date:2017-10-24

description: 
感知器
具体实现感知器步骤，
'''
import numpy as np
class Preception(object):

	"""
	eta: 学习效率
	n_iter:重复训练次数
	"""
	def __init__(self,eta=0.01,n_iter=10):
		self.eta =  eta
		self.n_iter = n_iter
	def fit(self,x,y):
		"""
		:param x: 训练需要的样本，x:[n_samples,n_features]
		x:[[1,2,3].[4,5,6]]
		那么，n_samples = 2 ,共有两个数组
		n_features = 3 表示有3类数据，或者是3列数据
		:param y: 表示种类 ，指的是训练的种类  根据x 的值，那么y:[1,-1] 共有1 和-1两种类型
		:return:
		z=w0*1  + w1*x1+...+wn*xn
		"""
		self.w_ = np.zeros(1+np.shape(x)) #初始化权重向量。初始化数组w_
		self.errors = [] #用于记录出现错误的item项
		for _ in range(self.n_iter):
			error = 0 #记录出现错误的值
			for  xi , target in zip(x,y):
				"""
				update =eta *  (y-y')
				"""
				update = self.eta *  (target -  self.predict(xi))
				self.w_[1:]  +=  update * xi
				self.w_[0]  += update
				error += int(update != 0,0) #
				self.errors.append(error)
	def net_input(self,X):
		"""
		函数功能：
		z = w0*1 + w1*x1+...+wn*xn
		:param X:
		:return:
		"""
		return np.dot(X,self.w_[1:] +self.w_[0])
	def predict(self,x):
		"""
		:param x:
		:return:
		"""
		return np.where(self.net_input(x) >=0,1,-1)

