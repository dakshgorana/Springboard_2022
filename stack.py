# Stack can be implemented using two ways
""" 1. Using list
    2. Using modules such as collection , dequeue

    It follows LIFO OR FILO

    Operations
     1. Push
     2. POP
     3. isEmpty
     4. top or peek
"""

class stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None for i in range(size)]

        self.top = -1

    def push(self,num):

        if self.top<self.size-1:
            self.top += 1
            self.stack[self.top] = num

        else:
            print("Stack is Full")


    def pop(self):
        if self.top != -1:
            temp = self.stack[self.top]
            self.stack[self.top] = None
            self.top -=1
            print(temp)
        else:
            raise IndexError("Stack is Full")



    def display(self):
        msg="bottom->"
        for i in range(self.size):
            if self.stack[i]!=None:
                msg = msg + str(self.stack[i])+"->"
            else:
                break
        print(msg)

    def is_Empty(self):
        if self.top == -1:
            return True
        else:
            return False


s = stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()

s.display()

#s.pop() will Invoke error as stack is empty and it is using pop

print(s.is_Empty())


