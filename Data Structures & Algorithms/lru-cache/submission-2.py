# create doubly linked list with left and right buffer nodes
class ListNode:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    # adds node to tail of list, updates right dummy pointer to point its prev to it
    def insert(self, node):
        tail, self.right.prev = self.right.prev, node
        tail.nxt, node.nxt, node.prev = node, self.right, tail

    # removes node from list, makes its prev point to its next and its next point to its prev
    def remove(self, node):
        node.prev.nxt, node.nxt.prev = node.nxt, node.prev


    # the cache is a dictionary where its key is the key itself, its value is the node
    # in the doubly linked list
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # dummy left and right pointers for inserting and deleting, init pointing to eachother
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        # item not in cache
        if key not in self.cache:
            return -1
        # otherwise item in cache was used, move it to the tail and return the value
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        # update existing key
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val = value
            return
        # not at capacity, just add node to cache
        if len(self.cache) < self.capacity:
            if key not in self.cache:
                self.cache[key] = ListNode(key, value)
                self.insert(self.cache[key])
        # at capacity, remove LRU node and add new one to tail
        else:
            self.cache[key] = ListNode(key, value)
            del self.cache[self.left.nxt.key]
            self.remove(self.left.nxt)
            self.insert(self.cache[key])
            
        
