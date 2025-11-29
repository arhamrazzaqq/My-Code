# SCOPE RESOLUTION = (LEGB) Local, Enclosing, Global, Built-in

#LOCAL SCOPE
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)
#--------------------------
#ENCLOSING SCOPE
def func1():
    x = 1
   
    def func2():
       x = 2
       print(x)
    func2()

func1()
#--------------------------
#GLOBAL SCOPE
def func1():
    print(x)

def func2():
    print(x)

x = 3

#--------------------------
#BUILT-IN SCOPE

from math import e

def func1():
    print(e)
e = 3

func1()
#--------------------------------------------------

