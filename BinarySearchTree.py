class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	
def inOrderTraversal(node):
	if node is None:
		return None
	inOrderTraversal(node.left)
	print(node.data,end=',')
	inOrderTraversal(node.right)
	

root=TreeNode(13)
node7=TreeNode(7)
node3=TreeNode(3)
node8=TreeNode(8)
node15=TreeNode(15)
node14=TreeNode(14)
node19=TreeNode(19)
node18=TreeNode(18)

root.left=node7
root.right=node15
node7.left=node3
node7.right=node8
node15.left=node14
node15.right=node19
node19.left=node18

inOrderTraversal(root)
print()

def search(node,target):
	if node.data==target:
		return node
	elif target < node.data:
		return search(node.left,target)
	else:
		return search(node.right,target)


result =search(root,8)
if result:
	print(f"\nFound the node with value :{result.data}")
else:
	print("\ntarget not found")

def insert(node,data):
	if node is None:
		return TreeNode(data)
	else:
		if data < node.data:
			node.left= insert(node.left,data)
		elif data > node.data:
			node.right=insert(node.right,data)
	return node
	

insert(root,10)
inOrderTraversal(root)
print()

def minValueNode(node):
	current=node
	while current.left is not None:
		current=current.left
	return current	

print("\nLowest value:",minValueNode(root).data)

def delete(node,data):
	if not node:
		return None
	if data < node.data:
		node.left=delete(node.left,data)
	elif data > node.data:
		node.right=delete(node.right,data)
	else:
		if not node.left:
			temp=node.right
			node=None
			return temp
		elif not node.right:
			temp=node.left
			node=None
			return temp
		else:
			node.data=minValueNode(node.right).data
			node.right=delete(node.right,node.data)
	return node


delete(root,15)
inOrderTraversal(root)
print()
































