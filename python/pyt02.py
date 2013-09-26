from ctypes import *
libc = CDLL("libc.so.6")
message_string = "Hello World!\n"
libc.printf("Testing: %d\n",libc.strlen(message_string))
