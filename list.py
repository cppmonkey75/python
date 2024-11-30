import math

def printList(l):
    for index,value in enumerate(l):
        print(f"idx {index} val {int(value)}")

squares=[1,4,9,16,24]
cube=[]
for item in squares:
    cube.append(pow(math.sqrt(item),3))
printList(cube)