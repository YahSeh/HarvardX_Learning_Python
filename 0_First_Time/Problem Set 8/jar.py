
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 :
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity :
            raise ValueError("The jar can't fit that many cookies")
        if self.size + n > self.capacity :
            raise ValueError("The jar can't fit that many cookies")
        self._size += n


    def withdraw(self, n):
        if self.size < n :
            raise ValueError("There aren't enough cookies to took ion the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
"""
def main() :
        jar = Jar()
        jar.deposit(2)
        jar.withdraw(1)
        print(jar)

if __name__ == "__main__":
    main()
"""
