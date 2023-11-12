#!/usr/bin/python3
"""module that demo's the base parent class
"""


class Base:
	"""the base class"""
	
	__nb_objects = 0

	"""constructor method"""
	def __init__(self, id=None):
		
		if id is not None:
			self.id = id

		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
