#ex1
import math

def func(n):
  n=n*math.pi/180.
  return n

n=int(input())
print(func(n))

#ex2
import math

def func(a,b,c):
  s=((c+b)/2)*a
  return s

a,b,c= map(int, input().split())
print(func(a,b,c))

#ex3
import math

def func(a,b):
  p=a*b
  a=b/(2*math.tan(func1(180 / a)))

  s = p * a / 2
  return s

def func1(n):
  n=n*math.pi/180.
  return n

a,b= map(int, input().split())
print(int(func(a,b)))

#ex4
import math

def func(a,b):
  s = a*b
  return s
a,b= map(int, input().split())
print(float(func(a,b)))