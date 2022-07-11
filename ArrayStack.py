class ArrayStack:
    def __init__(self):
        self._data = []

    def length(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)==0

    def push(self,e):
        return self._data.append(e)

    def top(self):
        if self.is_empty():
            print('Stack is empty ') 
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            print('Stack is empty ') 
        else:
            return self._data.pop()
    
    def element(self):
        return self._data        


if __name__== "__main__":
    obj = ArrayStack()
    print('Check empty ?',obj.is_empty())
    print('Add Element :',obj.push(3))
    print('Add Element :',obj.push(4))
    print('Add Element :',obj.push(1))
    print('Add Element :',obj.push(10))
    print('Element present :',obj.element())
    print('Length of Array :',obj.length())
    print('Top element : ',obj.top())
    print('Remove element :',obj.pop())
    print('Length of Array :',obj.length())
    print('Element present :',obj.element())