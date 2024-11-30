import copy

class my_class:
    
    def __init__(self, value):
        self.my_list=[]
        for i in range(value):
            self.my_list.append(i)

    def print(self):
        print (self.my_list)
    

print("demoing copy and move")
m=my_class(10)
shallow_copy=copy.copy(m)
deep_copy=copy.deepcopy(m)
for i in range(10):
    m.my_list[i]=i*2
shallow_copy.print()
deep_copy.print()