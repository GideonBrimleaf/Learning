import mxnet as mx
from mxnet import nd
mx.random.seed(1)

x = nd.ones((3,4))
x

y = nd.random_normal(0, 1, shape=(3, 4))
#first arg = loc (mean) second = scale (std dev)
y.shape
y.size

x+y
x*y
nd.exp(y)

nd.dot(x, y.T)

nd.elemwise_add(x,y, out=y)
#This is just a fancy way to add which directly places the 
#output in the same location as the input - more memory efficient

x[1,2] = 9.0
#Second row, third column value assignment

x[1:2,1:3]
#Multi-slicing!

x = nd.ones(shape=(3,3))
y = nd.arange(3)

z = nd.random_normal(0, 1, shape=(3, 4), ctx=mx.gpu(0))