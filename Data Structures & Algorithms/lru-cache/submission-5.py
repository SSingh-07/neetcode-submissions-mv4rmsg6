class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.length = 0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            self.length+=1
        self.cache[key]= value

        
        if self.length > self.capacity:
            self.cache.popitem(last=False)
            self.length-=1
        
