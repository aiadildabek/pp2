#ex1
import re
pattern = 'ab*'
mystr=str(input())
if re.fullmatch(pattern , mystr):
    print(mystr)

#ex2
import re
pattern='ab{2,3}'
mystr=str(input())
if re.fullmatch(pattern , mystr):
    print(mystr)

#ex3
import re
pattern='[a-z]+_[a-z]+'
mystr=str(input())
if re.fullmatch(pattern , mystr):
    print(mystr)

#ex4
import re
pattern='[A-Z][a-z]+$'
mystr=str(input())
if re.fullmatch(pattern , mystr):
    print(mystr)

#ex5
import re
pattern='a.*b$'
mystr=str(input())
if re.fullmatch(pattern , mystr):
    print(mystr)

#ex6
import re
from row import txt

mystr = re.sub("[.,\s]", ":", txt)
print(mystr)

#ex7

import re

def convertor(match):
    return match.group(0)[1].upper()

mystr = "snake_case_base_bibibibibi"
x = re.sub(r'_.', convertor, mystr)

print(x)

#ex8

import re

mystr = "SplitThisStringAtUpperCase"
a = re.findall('[A-Z][^A-Z]*', mystr)
print(a)

#ex9
import re

mystr = "ThisIsAStringWithCapitalWords"
a = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', mystr)

while(a != re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', a)):
    x = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', a)

print(a)

#ex10
import re

mystr = "camelCaseStringExample"
a = re.sub(r'(?<!^)(?=[A-Z])', '_', mystr).lower()
print(a)