class Jar:
    def __init__(self, capacity=12):
        if capacity % 1 != 0 or capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._cookie_num = 0

    def __str__(self):
        return '🍪' * self._cookie_num

    def deposit(self, n):
        if n % 1 != 0 or n + self._cookie_num > self._capacity:
            raise ValueError('Exceeds capacity')
        self._cookie_num += n

    def withdraw(self, n):
        if n % 1 != 0 or n > self._cookie_num:
            raise ValueError('Insufficient cookies')
        self._cookie_num -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookie_num


if __name__ == '__main__':
    jar = Jar(12)
    jar.deposit(3)
    jar.withdraw(2)
    jar.withdraw(1)
    print(jar.size)
    print(jar.capacity)
    print(jar)
