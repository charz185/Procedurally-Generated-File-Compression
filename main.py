import random
import time
import os
import string
import array
import math
import sys
import binascii
import base64
asciiList = []
binList = []

GeneralSize = 5

def inputToList(input):
  global asciiList
  for x in input:
    if x not in asciiList:
      asciiList.append(x)
  print(str(asciiList))


def ListCharToBinary(charIndex):
  return (format(charIndex, '0' + str(int(len(asciiList) / 2)) + 'b'))


def writeToBytes(inout):
  return bytearray(inout, 'utf-8')


def decToBinary(num):
  s = format(num, 'b')
  return int(s, 2).to_bytes((len(s) + 7) // 8, 'big')


def binaryToDec(byte):
  if byte != bytes(',', 'utf-8'):
    return int.from_bytes(byte, 'big')
  else:
    return ','


def generateData(seed, size):
  global asciiList
  random.seed(seed)
  asciiList2 = asciiList
  return str(''.join(random.choices(asciiList2, k=size)))


def seedtoData(index, size, seed):
  global asciiList
  temp = generateData(seed, index + size)[index:index + size]
  return (temp)

def Jot(data1, index, seed):
  global GeneralSize
  foundEfficientData = True
  size = GeneralSize
  gensize = size
  while (foundEfficientData):
    list2 = generateData(seed, gensize)
    data2 = data1[index:index + size]
    pos = list2.find(data2)
    if pos != -1:
      foundEfficientData = False
      return pos
    else:
      gensize += gensize


def jot2(data1, index):
  global GeneralSize
  length = len(data1)
  seed = 0
  while True:
    index = 0
    returnlist = []
    randomSeedNotFound = True
    while randomSeedNotFound:
      tic2 = time.perf_counter()
      result = Jot(data1, index, seed)
      toc2 = time.perf_counter()
      index += GeneralSize
      returnlist.append(result)
      
      print(str(index) + '/' + str(length) + ': ' + str((toc2 - tic2)))
      if index >= length:
        randomSeedNotFound = False
    str1 = ""
    for x in asciiList:
      str1 += x + " "
    str1 = str1[:-1]
    str1 += ";"
    returnlist.insert(0,seed)
    print(str(returnlist))
    for x in returnlist:
      str1 += v2r(x, base64List)+" "
    str1 = str1[:-1]
    print(str(sys.getsizeof(str1) - sys.getsizeof(data1)) + " " + str(seed))
    if sys.getsizeof(data1) > sys.getsizeof(str1):
      return str1
    else:
      seed += 1

def v2r(n, base): # value to representation https://stackoverflow.com/questions/54152762/python-compactly-and-reversibly-encode-large-integer-as-base64-or-base16-having
    """
    Convert a positive integer to its string representation in a custom base.
    
    :param n: the numeric value to be represented by the custom base
    :param base: the custom base defined as a string of characters, used as symbols of the base
    :returns: the string representation of natural number n in the custom base
    """
    if n == 0: 
      return base[0]
    b = len(base)
    digits = ''
    while n > 0:
        digits = base[n % b] + digits
        n  = n // b
    return digits
  
base64List='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_!@%^&+=/|~:;`[]{}()'

#https://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base/65744#65744
def r2v(digits, base): # representation to value
    """Compute the number represented by string 'digits' in a custom base."""
    b = len(base)
    n = 0
    for d in digits:
        n = b * n + base[:b].index(d)
    return n
  
def dataToSeed(data):
  randomSeedNotFound = True
  counter = 0
  timerList = []
  index = 0
  length = len(data)
  tic = time.perf_counter()
  returnlist = jot2(data, index)
  x = 0
  for i in os.listdir('encoded/'):
    x += 1
  f = open('encoded/Data' + str(x) + '.txt', 'w')
  f.write(returnlist)
  f.close()


def readFile(fileName):
  with open(fileName, 'r') as f:
    a = f.readline()
    b = a.split(';')
    c = b[1].split(",")
    print(str(c))
    z = []
    for x in b[0].split(" "):
      print(str(x))
      z.append(x)
    inputToList(z)
    c = c[0].split(" ")
    seed = r2v(c[0],base64List)
    c.pop(0)
    f.close()
    d = []
    print(str(c))
    for x in c:
      d.append(r2v(x,base64List))
    print(str(d))
    return [d, seed]


def CharToBinary(char):
  return str(format(ord(char), '08b'))


def readFileToUsableData(list1):
  list2 = []
  for z in list1:
    list2.append(z)
  print(str(list2))
  return list2


def FileToUsableDataToSeed(list1):
  usableDataList = []
  for x in list1:
    usableDataList.append(x)
  return usableDataList


random.seed(0)
x = input("y/n")
if x == 'y':
  list1 = readFile('encoded/Data95.txt')
  p = list1[0]
  k = ''
  list = ''
  print(str(asciiList))
  print("P: "+str(p))
  for x in p:
    tic1 = time.perf_counter()
    list += str(seedtoData(int(x), GeneralSize, list1[1]))
    toc1 = time.perf_counter()
    print(str(toc1 - tic1))
  print(str(list))
  x = 0
  for i in os.listdir('results/'):
    x += 1
  with open("results/sample"+str(x)+".txt", "w") as f1:
    f1.write(list)
elif x == "Rand#":
  num = int(input())
  str1 = ''.join(map(str,random.choices([1,2,3,4,5,6,7,8,9,0],k=num)))
  #for z in str0:
  #  str1 += CharToBinary(z)

  inputToList(str1)
  x = 0
  for i in os.listdir('collection/'):
    x += 1
  with open("collection/sample"+str(x)+".txt", "w") as f1:
    f1.write(str1)
  print(str(sys.getsizeof(str1)))
  #z = random.choices(['0', '1'], k=m)
  #str1 = ''.join(map(str, z))
  tic = time.perf_counter()
  dataToSeed(str1)
  toc = time.perf_counter()
  print(str(toc - tic))
elif x == "Image":
  y = input("Image#? ")
  imgb = ''
  GeneralSize = 4
  with open("input/Image"+str(y)+".png", "rb") as f:
     imgb = f.read()
  with open("collection/imageBin.txt","wb") as f2:
    f2.write(imgb)
  print(str(sys.getsizeof(imgb)))
  list1 = ''.join(map(str,imgb))
  
  inputToList(list1)
  print(str(asciiList))
  dataToSeed(list1)
else:
  #m = int(input("size")
  file = input("file? ")
  str0 = ''
  with open("input/Data"+file+".txt") as f:
    str0 = f.readlines()[0]
    
  #with open("test.txt",'r') as f:
   # x = f.readlines()
  str1 = str0
  #for z in str0:
  #  str1 += CharToBinary(z)

  inputToList(str1)
  x = 0
  for i in os.listdir('collection/'):
    x += 1
  with open("collection/sample"+str(x)+".txt", "w") as f1:
    f1.write(str1)
  print(str(sys.getsizeof(str1)))
  #z = random.choices(['0', '1'], k=m)
  #str1 = ''.join(map(str, z))
  tic = time.perf_counter()
  dataToSeed(str1)
  toc = time.perf_counter()
  print(str(toc - tic))