"""

class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

root=TreeNode('R')
NodeA=TreeNode('A')
NodeB=TreeNode('B')
NodeC=TreeNode('C')
NodeD=TreeNode('D')
NodeE=TreeNode('E')
NodeF=TreeNode('F')
NodeG=TreeNode('G')

root.left=NodeA
root.right=NodeB
NodeA.left=NodeC
NodeA.right=NodeD
NodeB.left=NodeE
NodeB.right=NodeF
NodeF.left=NodeG

def preOrderTraversal(Node):
	if (Node==None):
		return 	
	print(Node.data,end=',')
	preOrderTraversal(Node.left)
	preOrderTraversal(Node.right)


def inOrderTraversal(Node):
	if (Node==None):
		return 	
	
	inOrderTraversal(Node.left)
	print(Node.data,end=',')
	inOrderTraversal(Node.right)


def postOrderTraversal(Node):
	if (Node==None):
		return 	
	
	postOrderTraversal(Node.left)
	postOrderTraversal(Node.right)
	print(Node.data,end=',')


preOrderTraversal(root)
print()

inOrderTraversal(root)

print()

postOrderTraversal(root)
print()

binary_tree_array=['R','A','B','C','D','E','F',None,None,None,None,None,None,'G']
def left_child_index(index):
	return 2*index+1

def right_child_index(index):
	return 2*index+2


right_child=right_child_index(0)
left_child_of_right_child=left_child_index(right_child)

data=binary_tree_array[left_child_of_right_child]

print('root.right.left.data : ',data)

"""
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
	return 2*index+1

def right_child_index(index):
	return 2*index+2

def pre_order(index):
	if index >= len(binary_tree_array) or binary_tree_array[index] is None:
		return []
	return [binary_tree_array[index]]+pre_order(left_child_index(index))+pre_order(right_child_index(index))

def in_order(index):
	if index >=len(binary_tree_array) or binary_tree_array[index] is None:
		return []
	return in_order(left_child_index(index)) +[binary_tree_array[index]]+in_order(right_child_index(index))

def post_order(index):
	if index >=len(binary_tree_array) or binary_tree_array[index] is None:
		return []
	return post_order(left_child_index(index))+post_order(right_child_index(index)) +[binary_tree_array[index]]

print("Pre-order Traversal:", pre_order(0))
print("In-order Traversal:", in_order(0))
print("Post-order Traversal:", post_order(0))

































