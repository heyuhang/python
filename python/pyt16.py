# -*- coding:utf-8 _-*-
#Fibonacci数列模块
def fib(n):
    a, b = 0, 1
    if n ==1:
        print 1 
        while b < n:
            print b,
            a, b = b, a+b
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

