# -*- coding: utf-8 -*-
import cmd
import string, sys

class CLI(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = '>' # 定义命令提示符

	def do_hello(self, arg): # 定义hello命令执行的操作
		print "hello again", arg, "!"

	def help_hello(self):
		print "syntax: hello [message]",
		print "-- prints a hello message"

	def do_quit(self, arg):
		sys.exit(1)

	def help_quit(self):
		print "syntax: quit",
		print "-- terminates the application"
	
	# 定义quit的快捷方式
	do_q = do_quit

# 创建CLI实例
cli = CLI()
cli.cmdloop()
