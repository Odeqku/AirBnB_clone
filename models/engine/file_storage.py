
#!/usr/bin/python3

from models.base_model import BaseModel
import json

class FileStorage:

	__file_path = 'file.json'
	__objects = {}

	def all(self):
		return FileStorage.__objects

	def new(self, obj):
		print('hi')
		v = 'obj.__class__.__name__'
		FileStorage.__objects[f'{v}.{obj.id}'] = obj

	def save(self):
		print('hii')
		dic = FileStorage.__objects
		for k in dic:
			if isinstance(dic[k], datetime.datetime):
				dic[k] = dic[k].isoformat()
		with open(FileStorage.__file_path, 'w') as f:
			json.dump(dic, f)

	def reload(self):
		if FileStorage.__file_path:
			with open(FileStorage.__file_path, 'r') as f:
				FileStorage.__objects = json.load(f)
		else:
			pass
'''
storage = FileStorage()
storage.reload()
'''
