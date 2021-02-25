# hash values can be used to index for a value


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def get(self, key):  # __getitem__,  "tempHash['march 6']"" returns 130
        h = self.get_hash(key)
        # return self.arr[h]
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

    def add(self, key, val):  # __setitem__, "tempHash['march 6'] = 130"
        h = self.get_hash(key)
        #self.arr[h] = val

        # for collision, remember arr is now a 2d array:
        found = False
        for index, element in enumerate(self.arr[h]):
            # already have an element for this key
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def delete(self, key):
        h = self.get_hash(key)
        #self.arr[h] = None
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


if __name__ == '__main__':
    tempHash = HashTable()
    tempHash.add('march 6', 1)
    tempHash.add('march 12', 123)
    tempHash.add('march 20', 50)
    tempHash.add('march 1', 98)
    print(tempHash.arr)
    print(tempHash.get('march 1'))
    tempHash.delete("march 1")
    print(tempHash.arr)
