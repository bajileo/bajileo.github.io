class HashTable:
    
        def __init__(self):
               self.MAX = 10
               self.arr = [None for i in range(self.MAX)]
        
        def get_hash(self, key):
                hash = 0
                for char in key:
                        hash += ord(char)
                return hash % self.MAX
        
        def insert(self, key, value):
                index = self.get_hash(key)
                if self.arr[index] is None:
                        self.arr[index] = (key, value)
                else:
                        while self.arr[index] is not None:
                                index = (index + 1)% self.MAX
                self.arr[index] = (key, value)
        def search(self, key):
                index = self.get_hash(key)
                while self.arr[index] is not None:
                        if self.arr[index][0] == key:
                                return self.arr[index][1]
                        index = (index + 1) % self.MAX
                return None
        def delete(self, key):
                index = self.get_hash(key)
                while self.arr[index] is not None:
                        if self.arr[index][0] == key:
                                self.arr[index] = None
                                return
                        index = (index + 1) % self.MAX
        def display(self):
                for i in range(self.MAX):
                        if self.arr[i]:
                                print(f"Index {i}: {self.arr[i]}")
mytable = HashTable()
mytable.insert("march 1", 128)
mytable.insert("march 1", 211)
mytable.insert("march 4", 123)
mytable.insert("march 6", 93)
mytable.insert("march 17", 523)
mytable.delete("march 6")
mytable.display()
