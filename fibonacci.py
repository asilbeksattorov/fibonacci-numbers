""" First Version

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration()

fib = Fibonacci(10)
for num in fib:
    print(num)
"""



"""
# Second Version
class Fibonacci:
     def __init__(self, stop: int):
         self._start = 0
         self._stop = stop
         self._index = 0
         self._next = 1  # protected

     def __iter__(self):
         return self

     def __next__(self):
         if self._index >= self._stop:
             raise StopIteration('Index out of range')
         else:
             fibonacci = self._start
             self._start, self._next = self._next, self._start + self._next
             self._index += 1
             return fibonacci

fibo = Fibonacci(10)
for i in fibo:
    print(i)
"""



"""
def even_numbers(n):
     i = 0
     while i <= n:
        yield i
        i += 2

gen = even_numbers(100)
for i in gen:
    print(i)
"""



def fibonacci_generator(n):

    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

fibonacci_numbers = fibonacci_generator(10)

for num in fibonacci_numbers:
    print(num)



