class SimpleHashSet:
	def __init__(self,size):
		self.size=size
		self.buckets=[[] for _ in range (size)]
	
	def hash_function(self,value):
		return sum(ord(char)for char in value)%self.size
		
	def add(self,value):
		hash_code=self.hash_function(value)
		bucket=self.buckets[hash_code]
		bucket.append(value)
		
	def remove(self,value):
		hash_code=self.hash_function(value)
		bucket=self.buckets[hash_code]
		if value in bucket:
			bucket.remove(value)
		
	def contains(self,value):
		hash_code=self.hash_function(value)
		bucket=self.buckets[hash_code]
		return value in bucket
			
		
	def print_set(self):
		print("Hash set contains:")
		for index,value in enumerate(self.buckets):
			print(f"Bucket {index}: {value} ")
		
# Creating the Hash Set from the simulation
hash_set = SimpleHashSet(10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:",hash_set.contains('Peter'))
print("Removing 'Peter'")
hash_set.remove('Peter')
print("'Peter' is in the set:",hash_set.contains('Peter'))
print("'Adele' has hash code:",hash_set.hash_function('Adele'))

