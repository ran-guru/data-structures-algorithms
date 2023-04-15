class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        """Hash function"""
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def print_table(self):
        """Prints out all the key value pairs in the hash table"""
        for i, val in enumerate(self.data_map):
            print(i, ': ' , val)


    def set_item(self, key, value):
        """Set key value pair"""
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []   
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """Get value by key"""
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                
    def keys(self):
        """Returns all the keys in the hash table"""
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hash_table = HashTable()
my_hash_table.set_item('grapes', 10000)

my_hash_table.set_item('apples', 9)
my_hash_table.set_item('oranges', 2)
my_hash_table.set_item('mangoes', 3)
my_hash_table.set_item('bananas', 6)
my_hash_table.set_item('pineapples', 1)

apples = my_hash_table.get_item('apples')
keys = my_hash_table.keys()
print(keys)