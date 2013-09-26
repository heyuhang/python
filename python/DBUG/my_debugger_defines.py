# -*- coding:utf-8 -*-

from ctypes import *

WORD    = c_ushort
DWORD   = c_ulong
LPBYTE  = POINTER(c_ubyte)
LPTSTR  = POINTER(c_char)
HANDLE  = c_void_p

# 常值定义
DEBUG_PROCESS   =0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# 定义函数CreaterocessA()所需的结构提
class STARTUPINFO(Structure):
    _fields_=[
        ( "cb",         DWORD ),
        ( "lpReserved", LPTSTR),
        ( "lpDesktop",  LPTSTR),
        ( "lpTitle",    LPTSTR),
        ( "dwX",        DWORD),
        ( "dwY",        DWORD),
        ( "dwXSize",    DWORD),
        ( "dwYSize",    DWORD),
        ( "dwXCountChars",DWORD),
        ( "dwYCountChars",DWORD),
        ( "dwFillAttribute",DWORD),
        ( "dwFlags",    DWORD),
        ( "wShowWindow",DWORD),
        ( "cbReserved2",DWORD),
        ( "lpReserved2",DWORD),
        ( "hStdInput",  HANDLE),
        ( "hStdOutput", HANDLE),
        ( "hStdError",  HANDLE),
    ]
class PROCESS_INFORMATION(Structure):
    _fields_=[
        ( "hProcess",   HANDLE),
        ( "hThread",    HANDLE),
        ( "dwProcessId",DWORD),
        ( "dwThreadID", DOWRD),
    ]

