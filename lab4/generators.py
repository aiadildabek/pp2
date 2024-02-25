#ex1

class Squar:
  def __init__(self,n):
    self.n=n
  def __iter__(self):
    self.num=1
    return self
  def __next__(self):
    if self.num<=self.n:
      x = self.num**2
      self.num=self.num+1
      return x
    else:
      raise StopIteration
  
  
dildabek = Squar(10)
iterarr = iter(dildabek)

for i in iterarr:
 print(i)

#ex2
 
class Squar:
  def __init__(self,n):
    self.n=n
  def __iter__(self):
    self.num=0
    return self
  def __next__(self):
    self.num+=2
    if self.num>=self.n:
      raise StopIteration
    else:
      return self.num
  
dildabek = Squar(10)
iterarr = iter(dildabek)

for i in iterarr:
 print(i)
 
#ex3

class Squar:
  def __init__(self,n):
    self.n=n
  def __iter__(self):
    self.num=0
    return self
  def __next__(self):
    self.num+=12
    if self.num>=self.n:
      raise StopIteration
    else:
      return self.num
  
dildabek = Squar(124)
iterarr = iter(dildabek)

for i in iterarr:
 print(i)

#ex4
def mynum(n,m):
  while n<=m:
   yield n**2
   n+=1
dild=mynum(4,9)
for i in dild:
  print(i)

#ex5
def mynum(n):
  while n>=0:
   yield n
   n-=1
dild=mynum(8)
for i in dild:
  print(i)