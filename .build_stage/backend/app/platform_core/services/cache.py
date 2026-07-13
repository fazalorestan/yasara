class Cache:
    def __init__(self): self._data={}
    def set(self,k,v): self._data[k]=v
    def get(self,k,default=None): return self._data.get(k,default)
cache=Cache()
