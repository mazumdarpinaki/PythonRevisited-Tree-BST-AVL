def hashFunction(value):
	return sum(ord(char) for char in value)%10 # assuming size=10
def add (value):
	index=hashFunction(value)
	bucket=hash_set[index]
	if value not in bucket:
		bucket.append(value)

def remove(value):
	index=hashFunction(value)
	bucket=hash_set[index]
	if value in bucket:
		bucket.remove(value)

def contains(value):
	index=hashFunction(value)
	bucket=hash_set[index]
	return value in bucket
	
def size():
	size=0
	for value in hash_set:
		size+=1
	return size

def print_set(hash_set):
	for index,bucket in enumerate(hash_set):
		print(f"Bucket {index} : {bucket}")

hash_set=[[],[],[],[],[],[],[],[],[],[]]
add("Charlotte")
add("Thomas")
add("Jens")
add("Peter")
add("Lisa")
add("Adele")
add("Michaela")
add("Bob")

print_set(hash_set)
print(remove("Bob"))
print(contains("Lisa"))
print(size())


