class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = ListNode(0, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        elif len(self.d) >= self.capacity:
            self.pop()
        node = ListNode(key, value)
        self.d[key] = node
        self.insert(node)

    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop(self) -> None:
        if len(self.d) == 0:
            return
        node = self.tail.prev
        del self.d[node.key]
        self.remove(node)

    def insert(self, node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)