#!/usr/bin/python3

from models
import json

class FileStorage:

	__file_path = 'file.json'
	__objects = {}

	def all(self):
		return FileStorage.__objects

	def new(self, obj):
		v = 'obj.__class__.__name__'
		FileStorage.__objects[f'{v}.{obj.id}'] = obj

	def save(self):
		dic = FileStorage.__objects
		with open(FileStorage.__file_path, 'w') as f:
			json.dump(dic.to_dict(), f)

	def reload(self):

		if FileStorage.__file_path:
			print("Hi")
			with open(FileStorage.__file_path, 'r') as f:
				FileStorage.__objects = json.load(f)
		else:
			pass

#from models.base_model import BaseModel
