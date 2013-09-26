# -*- coding:utf-8 -*-

from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass

    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS

        startupinfo = STARTUPINFO()
        process_infomation = PROCESS_INFORMATION()

        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow= 0x0
        startupinfo.cb=sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe, None, creation_flags, None, None,byref(startupinfo), byref(process_information)):
            print "[*] We have sucessfully launched the process!"
            print "[*] PID: %d" % process_infomation.dwProcessId
        else:
            print "[*] Error: 0x%08x." %kernel32.GetLastError()
