class SimpleHashMap:
	def __init__(self,size):
		self.size=size
		self.buckets=[[] for _ in range(size)]

	def hash_function(self,key):
		return sum(int(char)for char in key if char.isdigit())%10
	
	def get(self,key):
		hash_code=self.hash_function(key)
		bucket=self.buckets[hash_code]
		for k,v in bucket:
			if k==key:
				return v
		return None
	def put(self,key,value):
		hash_code=self.hash_function(key)
		bucket=self.buckets[hash_code]
		for i,(k,v) in enumerate(bucket):
			if k==key:
				bucket[i]=(key,value)
		bucket.append((key,value))

	def remove(self,key):
		hash_code=self.hash_function(key)
		bucket=self.buckets[hash_code]
		for i,(k,v) in enumerate(bucket):
			if k==key:
				del bucket[i]

	def print_map(self):
		print("Hash map contains:")
		for index,bucket in enumerate(self.buckets):
			print(f"Bucket {index}: {bucket}")





hash_map = SimpleHashMap(size=10)

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

# Checking if Peter is still there
print("Name associated with '123-4570':", hash_map.get("123-4570"))
