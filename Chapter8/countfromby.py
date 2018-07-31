class CountFromBy:
    def __init__(self, v:int, i:int) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr
h = CountFromBy(100, 10)
print(h.val)
print(h.incr)
h.increase()
print(h.val)
