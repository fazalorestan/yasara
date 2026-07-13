class Queue:
    def __init__(self): self._items=[]
    def push(self,item): self._items.append(item)
    def pop(self): return self._items.pop(0) if self._items else None
    def size(self): return len(self._items)
queue=Queue()
