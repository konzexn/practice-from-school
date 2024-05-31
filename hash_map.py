class hash_table:
    def __init__(self, size):
        self.size = size
        self.table = self.create_table(size)

    def create_table(self, size):
        return [[for i in range(size)] for j in range(size)]

    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.table[hashed_key]
        found_key = False
        for index, recode in enumerate(bucket):
            rec_key, rec_val = recode
            if rec_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.table[hashed_key]
        found_key = False
        for index, recode in enumerate(bucket):
            rec_key, rec_val = recode
            if rec_key == key:
                found_key = True
                break
        if found_key:
            return rec_val
        else:
            return "No record found"

    def del_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.table[hashed_key]
        found_key = False
        for index,recode in enumerate(bucket):
            rec_key, rec_val = recode
            if rec_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
            return
    def __str__(self):
        return "".join(str(item) for item in self.table)

hash_table = hash_table(10)

hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()