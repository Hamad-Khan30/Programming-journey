class Counter:
    def __init__(self):
        self._count = 0  
    
    def increment(self):
        self._count += 1
    
    def value(self):
        return self._count
    
    def set_count(self, new_value):
        if new_value < 0:
            print("Error: Count can not be negative")
        else:
            self._count = new_value

counter = Counter()

print(f"Initial count: {counter.value()}")  

counter.increment()
counter.increment()
counter.increment()
print(f"After 3 increments: {counter.value()}")  

counter.set_count(-5)  
print(f"After invalid set: {counter.value()}")  

counter.set_count(10)
print(f"After valid set: {counter.value()}")  
print(f"Internal count: {counter._count}")  