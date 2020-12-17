class Node:
	value = None
	next_ptr = None
	
	def __init__(self, value, next_ptr=None):
		self.value = value
		self.next_ptr = next_ptr


	def __init__(self):
		self.value = None
		self.next_ptr = None
