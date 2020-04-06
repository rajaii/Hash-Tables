# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        
        OPTIONAL STRETCH: Research and implement DJB2
        '''
         # Start from an arbitrary large prime
        hash_value = 5381
        # Bit-shift and sum value for each character
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)

        if self.count == self.capacity:
            self.resize()
        
        self.storage[hash_key] = value

        self.count += 0

        return self.storage[hash_key]



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)

        if not self.retrieve(key):
            print(f'Warning!! {key} is not an actual key for this hash table!')

        else:
            self.storage[hash_key] = None
        count -= 1

        return self.storage

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_key = self._hash_mod(key)
        return self.storage[hash_key]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")

    h = HashTable(8)

    h.insert("key-0", "val-0")
    h.insert("key-1", "val-1")
    h.insert("key-2", "val-2")
    h.insert("key-3", "val-3")
    h.insert("key-4", "val-4")
    h.insert("key-5", "val-5")
    h.insert("key-6", "val-6")
    h.insert("key-7", "val-7")
    # ht.insert("key-8", "val-8")
    # ht.insert("key-9", "val-9")

    print(h.retrieve('key-0'))
    print(h.retrieve('key-7'))

    



