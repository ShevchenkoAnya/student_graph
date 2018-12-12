import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import random as ra
def line ():
    x = np.linspace(-10, 10, 20)
    y = x**2
    plt.plot(x, y)
    plt.show()
line()
def stolb():
    x=[]
    y=[]
    for i in range(10):
        a = ra.randint(1,20)
        b = ra.randint(1,20)
        x.append(a)
        y.append(b) 
    plt.bar(x, y, label='bars1')
    plt.legend()
    plt.show()
def scatter():
    x=[]
    y=[]
    for i in range(100):
        x.append(i)
        y.append(i)
    plt.scatter(x, y, label='bars1')
    plt.legend()
    plt.show()
def center():
    x=[]
    #y=[]
    for i in range(10):
        a = ra.randint(1,20)
       # b = ra.randint(1,20)
        x.append(a)
       # y.append(b)
    print(x)
    c=sum(x)/len(x)
    print(c)
def vari():
    x=[]
    #y=[]
    for i in range(10):
        a = ra.randint(1,20)
       # b = ra.randint(1,20)
        x.append(a)
       # y.append(b)
    a=sum(x)/len(x)
    c=((sum(x)-a)**2)/(len(x)-1)
    print(x)
    print(c)
def colle():
    x=[]
    y=[]
    for i in range(10):
        a = ra.randint(1,20)
        b = ra.randint(1,20)
        x.append(a)
        y.append(b)
    c=np.corrcoef(x,y)[0,1]
    print(c)
