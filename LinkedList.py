from Node import Node


class LinkedList:

	def __init__(self):
		self.__head = None
		self.__tail = None


	# method to add value in the front of the list
	def add_first(self, value):
		node = Node(value)
		if self.__head == None:
			self.__head = node
			self.__tail = node
		else:
			node.next_ptr = self.__head
			self.__head = node


	# method to add value at the end of the list
	def add_last(self, value):
		if self.__tail != None:
			node = Node(value)
			self.__tail.next_ptr = node
			self.__tail = node		
		else: 
			self.__head = self.__tail = node	


	# remove item from the list front 
	def remove_front(self):
		self.__head = self.__head.next_ptr

	# display the list items
	def display(self):
		itrator = self.__head
		while itrator != None:
			print(itrator.value)
			itrator = itrator.next_ptr

