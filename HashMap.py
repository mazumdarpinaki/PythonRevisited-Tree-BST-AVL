class SimpleHashMap:
	def __init__(self,size):
		self.size=size
		self.buckets=[[] for _ in range(size)]


	def hashFunction(self,key):
		return sum(int(chr) for chr in key if chr.isdigit())%self.size


	def put(self,key,value):
		index=self.hashFunction(key)
		bucket=self.buckets[index]
		for i,(k,v) in enumerate(bucket):
			if (k==key):
				bucket[i]=(key,value)
		
		bucket.append((key,value))

	def get(self,key):
		index=self.hashFunction(key)
		bucket=self.buckets[index]
		for k,v in bucket:
			if k==key:
				return v
		return None

	def remove(self,key):
		index=hashFunction(key)
		bucket=self.buckets[index]
		for i,(k,v) in enumerate(self.buckets):
			if k==key:
				del bucket[i]

	def print_map(self):

		for i,bucket in enumerate(self.buckets):
			print(f"Bucket {i} : {bucket}")


# Creating the Hash Map from the simulation
hash_map = SimpleHashMap(10)

# Adding some entries
hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()

# Demonstrating retrieval
print("\nName associated with '123-4570':", hash_map.get("123-4570"))

print("Updating the name for '123-4570' to 'James'")
hash_map.put("123-4570","James")
