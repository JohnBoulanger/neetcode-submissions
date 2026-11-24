class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}                      # key -> node
        self.left, self.right = Node(), Node()
        # left = LRU end, right = most recent end
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):                  # put just before right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)                    # mark as most recent
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])     # drop the old node
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next             # least recent
            self.remove(lru)
            del self.cache[lru.key]