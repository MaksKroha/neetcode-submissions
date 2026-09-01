class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashes = {}
        self.head = Node(0, 0, None, None)
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.hashes:
            return -1

        if self.head.next != self.hashes[key]:
            self.hashes[key].prev.next = self.hashes[key].next

            if self.tail == self.hashes[key]:
                self.tail = self.hashes[key].prev
            else:
                self.hashes[key].next.prev = self.hashes[key].prev

            self.hashes[key].prev = None
            self.hashes[key].next = self.head.next

            self.head.next.prev = self.hashes[key]
            self.head.next = self.hashes[key]

        return self.hashes[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.hashes:
            if len(self.hashes) == self.capacity:
                del self.hashes[self.tail.key]
                
                if self.head.next == self.tail:
                    self.head.next = None
                    self.tail = None
                else:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
        
            node = Node(key, value, None, self.head.next)
            if self.head.next is None:
                self.tail = node
            else:
                self.head.next.prev = node
            self.head.next = node
            self.hashes[key] = node
        else:
            self.hashes[key].val = value
            self.get(key)
    
        
