#ex1
list=[1,5,8,9,6]
sum=0
for x in list:
    sum+=x
print(sum)

#ex2
str="Hello World. Hello KBTU"

def counter(str):
    count_up, count_down=0, 0
    for i in str:
        if i.isupper():
            count_up += 1
        if i.islower():
            count_down += 1
            
    print(f"Upper case letters: {count_up}")
    print(f"Lower case letters:{count_down}")

counter(str)
#ex3
str=input()
def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
    
print(palindrome(str))

#ex4
from time import sleep

root = int(input())
delaychik = int(input())

sleep(delaychik / 1000)
print(f'Square root of {root} after {delaychik} milisconds is {root ** 0.5}')

#ex5
def func(arr):
    return all(arr)
arr=(1,3,5)
print(func(arr))