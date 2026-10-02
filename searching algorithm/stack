class Stack:
    def __init__(self):
      self._a=[]
      self.top=None
    def peek(self):
      if self._top is None:
        return "No elements"
      return self._a[self._top]
    def push(self,data):
      if self._top is None:
        ar=[0]
        self._top=0
        ar[self._top]=data
        self._a=ar
      else:
        ar=[0 for i in range(self._top+2)]
        for i in range(self._top+1):
          ar[i]=self._a[i]
        ar[-1]=data
        self._a=ar
        self._top+=1
  stack=Stack()
  stack.push(10)
  stack.push(20)
  print(stack.peek())
  