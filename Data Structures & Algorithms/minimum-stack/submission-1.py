class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        # if no value on minstack, or new value is new smallest, add it to minstack
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        # add to our regular stack as well
        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        # if the value we are popping is the current minimum of the stack
        # remove it from mins stack as well 
        if top == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
