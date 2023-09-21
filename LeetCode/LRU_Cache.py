# https://leetcode.com/problems/lru-cache/
class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next  
        self.prev = prev  

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = {}
        self.head = None
        self.tail = None

    def move_to_front(self, key: int) -> None:
        if self.hash_table[key] != self.head:
            if self.hash_table[key] == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                prev_node = self.hash_table[key].prev
                next_node = self.hash_table[key].next
                prev_node.next = next_node
                next_node.prev = prev_node
            self.update_head(key)

    def update_head(self, key: int) -> None:
        self.head.prev = self.hash_table[key]
        self.hash_table[key].next = self.head
        self.hash_table[key].prev = None
        self.head = self.hash_table[key]

    def get(self, key: int) -> int:
        if key not in self.hash_table:
            return -1

        self.move_to_front(key)
        return self.hash_table[key].val
    
    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            self.hash_table[key].val = value
            self.move_to_front(key)
        else:
            self.hash_table[key] = ListNode(key, value)
            if not self.head:
                self.head = self.head.next = self.tail = self.tail.prev = self.hash_table[key]
            else:
                if len(self.hash_table) > self.capacity:
                    del self.hash_table[self.tail.key]
                    prev_node = self.tail.prev
                    prev_node.next = None
                    self.tail = prev_node
                self.update_head(key)
        if self.capacity == 1:
            self.tail = self.head.next = self.tail.prev = self.head
            self.tail.next = None


result = [None]
lRUCache = None
# actions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# nums = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
actions = ["LRUCache","get","get","put","get","put","put","put","put","get","put"]
nums = [[1],[6],[8],[12,1],[2],[15,11],[5,2],[1,15],[4,2],[5],[15,15]]

actions_len = len(actions)
for i in range(actions_len):
    if actions[i] == "LRUCache":
        lRUCache = LRUCache(nums[i][0])
    elif actions[i] == "put":
        result.append(lRUCache.put(nums[i][0], nums[i][1]))
    elif actions[i] == "get":
        result.append(lRUCache.get(nums[i][0]))
    
print(result)