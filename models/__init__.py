#!/usr/bin/python2

from models.engine.file_storage import FileStorage

try:
	storage = FileStorage()
	"""Loading the json string back to the dictionary"""
	storage.reload()

except FileNotFoundError:
	pass

