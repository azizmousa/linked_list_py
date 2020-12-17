from Node import Node


class LinkedList:

	def __init__(self):
		self.__head = None
		self.__tail = None

	def add_first(self, value):
		node = Node()
		node.value = value
		if self.__head == None:
			self.__head = node
			self.__tail = node
		else:
			node.next_ptr = self.__head
			self.__head = node

	def add_last(self, value):
		if self.__tail != None:
			node = Node(value)
			self.__tail.next_ptr = node
			self.__tail = node		
		else: 
			self.__head = self.__tail = node	

	def display(self):
		itrator = self.__head
		while itrator != None:
			print(itrator.value)
			itrator = itrator.next_ptr

