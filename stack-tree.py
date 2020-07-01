class Node:
    def __init__(self, _value):
        self.value = _value
        self.left = None
        self.right = None

    def addChild(self,value):
        if(self.value > value and self.left != None):
            self.left.addChild(value)
        elif(self.value < value and self.right != None):
            self.right.addChild(value)
        elif(self.value > value and self.left == None):
            self.left = Node(value)
        elif(self.value < value and self.right == None):
            self.right = Node(value)

def inOrder(curr):
    if(curr.left != None):
        inOrder(curr.left)
    final.append(curr.value)
    if(curr.right != None):
        inOrder(curr.right)

def stackTrace(curr):
    stack = []
    prevNone = True
    stack.append(curr)
    while(len(stack)>0):
        curr = stack.pop(len(stack)-1)
        print(curr.value)
        if(curr.left != None):
            stack.append(curr.left)
        if(curr.right != None):
            stack.append(curr.right)

final =[]
list1 = [6, 1, 9, 4, 10, 27, 8]
if(len(list1)>0):
    root = Node(list1[0])
for i in range(1,len(list1)): 
    root.addChild(list1[i])
stackTrace(root)