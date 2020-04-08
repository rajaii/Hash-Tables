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

    def __str__(self):
        return f'<{self.key}, {self.value}>'


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
        #hashmod the key to find bucket
        index = self._hash_mod(key)

        if self.count >= self.capacity:
            self.resize()

        #check if a pair already exists in the bucket
        pair = self.storage[index]
        if pair is not None and pair.key == key:
            #if so add new pair to linkedpair that is stored
            pair.key = key
            pair.value = value
        elif pair is not None and pair.key != key:
            if pair.next is not None and pair.next.key == key:
                pair.next.value = value
            else:
                while pair.next is not None:
                    current = pair
                    nxt = pair.next
                    if nxt.key == key:
                        nxt.value = value
                    pair = nxt
                if pair.next is None:
                    pair.next = LinkedPair(key, value)
                    self.count += 1
        else:
            #if not, Create a new linkedpair and place it in the bucket
            self.storage[index] = LinkedPair(key, value)
            self.count += 1

        

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # Check if a pair exists in the bucket with matching keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # If so, remove that pair
            self.storage[index] = None
            self.storage -= 1
        elif self.storage[index] is not None and self.storage[index].key != key:
            if self.storage[index].next.key == key:
                self.storage[index].next = None
            else:
                print('Warninge: key does not exist')
        else:
            # Else print warning
            print("Warning: Key does not exist")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
       
         # Get the index from hashmod
        index = self._hash_mod(key)

        # Check if a pair exists in the bucket with matching keys
        # print(f'index: {index}')
        if self.storage[index] is not None and self.storage[index].key == key:
            # If so, return the value
            return self.storage[index].value
        elif self.storage[index] is not None and self.storage[index].key != key:
            # Else return None
            return self.storage[index].next.value
        else:
            return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        
        # for i in self.storage:
        #     if i is None:
        #         continue
        #     new_key = self._hash_mod(i.key)
        #     print(f'i = {i.key}, new_key = {new_key}')
        #     new_storage[new_key] = self.storage[i.key]

        for i in range(len(self.storage)-1):
            if self.storage[i] is None:
                continue
            elif self.storage[i].next is None:
                new_key = self._hash_mod(self.storage[i].key)
                print(f'i = {self.storage[i]}, new_key = {new_key}')
                #if there is a pair housed in newstorage at the new key
                if new_storage[new_key]:
                    #set the next of that to be a new lp
                    new_storage[new_key].next = LinkedPair(self.storage[i].key, self.storage[i].value)
                else:
                    new_storage[new_key] = self.storage[i]
            elif self.storage[i].next is not None:
                new_key1 = self._hash_mod(self.storage[i].key)
                new_key2 = self._hash_mod(self.storage[i].next.key)
                if new_storage[new_key1]:
                    new_storage[new_key1].next = LinkedPair(self.storage[i].key, self.storage[i].value)
                else:
                    new_storage[new_key1] = self.storage[i]
                if new_storage[new_key2]:
                    new_storage[new_key2].next = LinkedPair(self.storage[i].next.key, self.storage[i].next.value)
                else:
                    new_storage[new_key2] = self.storage[i].next


        self.storage = new_storage
        



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
   

   
