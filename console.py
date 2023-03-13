#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
	
	"""prompt charater"""
	prompt = '(hbnb) '


	def do_EOF(self, line):
		"""Exit the console application"""
		return True

	def do_quit(self, line):
		"""Quit commend to exit the program"""
		return True


if __name__ == "__main__":
	HBNBCommand().cmdloop()
