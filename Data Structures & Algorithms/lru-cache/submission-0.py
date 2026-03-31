class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.Next= None
        self.Prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left ,self.right = Node(0,0), Node(0,0)
        self.left.Next, self.right.Prev = self.right, self.left


    def insert(self, node):
        prev, Next = self.right.Prev, self.right
        prev.Next, Next.Prev = node, node
        node.Prev, node.Next = prev, Next
    
    def remove(self, node):
        prev, Next = node.Prev, node.Next
        prev.Next, Next.Prev = Next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru = self.left.Next
            self.remove(lru)
            del self.cache[lru.key]
            



        
        
