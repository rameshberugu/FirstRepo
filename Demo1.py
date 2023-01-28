import sys

sys.api_version
print("python version")

def add(a,b):
    return a+b
    

print("add " ,add(2,3),sys.api_version)

# if
print("------If------")
if(1==1):
    print ("true")
else:
    print("false")

print("-----end if ----")

#while
num=0
while(num<=4):
    print("integer ",num)
    num =num +1



#dictionary

keyValues =dict({1:"one",2:"two"})
print("dictionary",keyValues)

keyValues[3]="three"
keyValues[1]="ONE"
keyValues[4]="four"
print("dictionary",keyValues)

del keyValues[4]

print("dictionary",keyValues)
print("keys",keyValues.keys())
print("values",keyValues.values())

#tuple
tuple =("a", "b", "c")
print("tuple", tuple)

#for


#try catch

# import module in other path

#inheritance
print("----- add ----")
class A:
    a=0
    def add(self,a,b):
        return a+b
class B(A):
    def sub(self,a,b):
        return a-b

obj=B()
print("add ",obj.add(2,3))

#interface

#class

#tuple



