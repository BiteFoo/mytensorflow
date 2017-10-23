# -*- coding:UTF- -*- 
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import sys,os


def getstart():
    print 'get start  make sure active  virtualenv '
    print 'use: source ~/MachineLearning/bin/activate'
    print 'and csh ~/MachineLearning/bin/activate.csh,if csh is not command '\
    'you should use sudo apt-get install csh,and use command again! '

#def get_input_data(path=None):
#    cur_path = sys.path[0]+os.sep+path
 #   if not os.path.isdir(cur_path):
  #      return 
#    data_set = input_data.read_data_sets('MNIST_data',one_hot=True)

def start_soft_max():
    mnist = input_data.read_data_sets("MNIST_data",one_hot =True)
 #在构建图之前，创建会话对象，方便在运行时插入一些构建计算的图
    sess = tf.InteractiveSession()
#准备两个占位符变量，可以在运行时更改这两个值
    x = tf.placeholder(tf.float32,shape=[None,784])#图片数量矩阵 ，每正图片的像素点矩阵为28*38 =748
    y_ = tf.placeholder(tf.float32,shape=[None,10])#可以取到值的矩阵,图片可以取的值为0-9共10个
   #初始化权重值 w,和偏置值b
    w = tf.Variable(tf.zeros([784,10]))#表示有748个特征值和10个输出值
    b = tf.Variable(tf.zeros([10]))#共有10个数字，则有10中分类
    #所有变量都需要在执行session.run()方法之前，做好初始化工作
    #sess.run(tf.global_variables.initializer())
    sess.run(tf.global_variables_initializer())
#    sess.run(tf.initialize_all_variables())
    #实现regression模型和损失函数
    y = tf.matmul(x,w)+b  # tf.nn.softmax(tf.matmul(x*w)+b) #regression函数 ，预测函数
   # cross_entropy =  -tf_reduce_sum(y_*tf.log(y)) #交叉熵函数，计算损失函数
    #cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(lables = y_,logits =y))    
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
#训练模型
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
   # for i in range(1000):
    #    batch =mnist.train.next_batch(100)
     #   train_step.run(feed_dict={x:batch[0],y_:batch[1]}) 
    for _ in range(1000):
         batch = mnist.train.next_batch(100)
        # print(type(batch),',',batch)
         #print (batch[0])
         #print('=====================================================')
        # print (batch[1])
         train_step.run(feed_dict={x: batch[0], y_: batch[1]})
    #查找那些lable预测正确，因为这里选用了梯度下降算法，每次迭代下降为0.01,那么使用max找到概率最大的值
    print('y=',tf.argmax(y,1))
    print('y_= ',tf.argmax(y_,1))
    correct_prediction= tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
    print("correct_prediction=",correct_prediction)
    #输出最后的结果比率
    accurary = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    print("accurary = ",accurary)
    print (accurary.eval(feed_dict={x:mnist.test.images,y_:mnist.test.labels})) 
    sess.close()
    

def tensorflow_demo1():
    matrix1 = tf.constant([[3.,3.]])
    matrix2 =  tf.constant([[2.],[2.]])
    product=  tf.matmul(matrix1,matrix2)
    sess = tf.Session()
    result = sess.run(product)
    print result
    sess.close()


if __name__=='__main__':
   # getstart()
   #tensorflow_demo1()
#   get_input_data("")
    start_soft_max()
