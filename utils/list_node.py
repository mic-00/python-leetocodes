from typing import Self

class ListNode(object):
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next
    
    def fromValues(*values: int) -> Self:
        if len(values) == 0:
            return None
        return ListNode(values[0], ListNode.fromValues(*values[1:]))
    
    def get(self, i: int) -> Self:
        if i == 0:
            return self
        return self.next.get(i - 1)
    
    def getStringRepresentation(self) -> str:
        if not self.next:
            return f"{self.val}"
        return f"{self.val} -> {self.next.getStringRepresentation()}"
    
    def length(self):
        if not self.next:
            return 1
        return 1 + self.next.length()