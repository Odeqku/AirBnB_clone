#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage()
'''Loading the json string back to the dictionary'''
storage.reload()
