import math

def printList(l):
    for index,value in enumerate(l):
        print(f"idx {index} val {int(value)}")

squares=[1,4,9,16,24]
cubes=[]
for item in squares:
    cubes.append(pow(math.sqrt(item),3))
printList(cubes)
squares.clear()
for i in range(10):
    squares.append(i*i)
print(squares)
cubes.clear()
for i in range(10):
    cubes.append(i*squares[i])
print (cubes)
squares_cubes_map = dict([squares,cubes])
for square,cube in enumerate(squares_cubes_map):
    print(f"{square}=>{cube}")
