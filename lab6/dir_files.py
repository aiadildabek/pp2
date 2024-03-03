#ex1

import os

def only_dir(path):
    listik = [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]
    print(listik)


def only_files(path):
    listik = [dir for dir in os.listdir(path) if os.path.isfile(os.path.join(path, dir))]
    print(listik)


def doublegis(path):
    listik = [dir for dir in os.listdir(path)]
    print(listik)


path = "/pp2-labki" 
doublegis(path)
only_dir(path)
only_files(path)

#ex2
import os

def checker(path):
    if os.access(path, os.F_OK):
        print("The path exists")
    else:
        print("The path does not exists")

    if os.access(path, os.R_OK):
        print("The path is readable")
    else:
        print("The path is not readable")
    
    if os.access(path, os.W_OK):
        print("The path is writable")
    else:
        print("The path is not writable")
    
    if os.access(path, os.X_OK):
        print("The path is executable")
    else:
        print("The path is not executable")


direct = os.getcwd()
pathik = os.path.join(direct, "something.txt")

print(pathik)
checker(pathik)

#ex3
import os

direct = os.getcwd()
path = os.path.join(direct, "something.txt")

if not os.access(path, os.F_OK):
    print("The path does not exist")
else:
    print(f'Filename is: {os.path.basename(path)}')
    print(f'Directory portion is: {os.path.dirname(path)}')

#ex4
import os 

direct = os.getcwd()
path = os.path.join(direct, "something.txt")

f, counter = open(path, "r"), 0
for _ in f:
    counter += 1

print(counter)
#ex5
file_name = "something2.txt"
some_list = ['data', str(2), str(3)]

f = open(file_name, "a")
for i in some_list:
    f.write(str(i) + ' ')
f.close()

#ex6
file_name = 'A'
while file_name != 'Z':
    f = open(f'{file_name}.txt', "a")
    f.close()
    file_name = chr(ord(file_name) + 1)
#ex7
file_name, to_copy, text = "something.txt", "something2.txt", ""

f = open(file_name, "r")
text = f.read()
f.close()

f = open(to_copy, "w")
f.write(text)
f.close()
#eex8

import os

def checker(path):
    if not os.access(path, os.F_OK):
        return False

    if not os.access(path, os.X_OK):
        return False
    
    return True

direct = os.getcwd()
path = os.path.join(direct, "something3.txt")

if(checker(path)):
    os.remove(path)
else:
    print("Create a file named something3.txt pls")
