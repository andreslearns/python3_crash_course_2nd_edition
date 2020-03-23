#!/usr/bin/env python3
from Exscript import Queue
from Exscript.util.decorator import autologin
from Exscript.util.file import get_hosts_from_file, get_accounts_from_file
from netaddr import valid_ipv4
from colorama import *

print ('-' * 60)
print ("\t\tCLI BASE DDOS MITIGATION SCRIPT")
print ('-' * 60)
task = input("TASK:DIVERT/NO_DIVERT\t: ")
wildcard = '0.0.0.255 any'
ipaddr = input(f"\nIP BLOCK\t\t: ")

global acl_normal

@autologin()

def do_something(job, host, conn):
    
    if task == 'DIVERT' and valid_ipv4(ipaddr):
        conn.execute('term len 0')
        conn.execute('show ip access-list NORMAL\n')
        acl_normal = (conn.response)
        conn.execute('conf t')
        conn.execute('ip access-list extended NORMAL')
        conn.execute('no permit ip any any')
        conn.execute(f"deny ip {ipaddr} {wildcard}")
        conn.execute(f"permit ip any any")
        
        conn.execute('ip access-list extended DIVERT')
        conn.execute('no deny ip any any')
        conn.execute(f"permit ip {ipaddr} {wildcard}")
        conn.execute('deny ip any any')
        conn.execute('end')
        conn.execute('clear ip bgp * soft out')
        print (acl_normal)
        
    elif task == 'NO_DIVERT' and valid_ipv4(ipaddr):
        conn.execute('term len 0')
        conn.execute('conf t')
        conn.execute('ip access-list extended NORMAL')
        conn.execute('no permit ip any any')
        conn.execute(f"no deny ip {ipaddr} {wildcard}")
        conn.execute(f"permit ip any any")
        
        conn.execute('ip access-list extended DIVERT')
        conn.execute('no deny ip any any')
        conn.execute(f"no permit ip {ipaddr} {wildcard}")
        conn.execute('deny ip any any')
        conn.execute('end')
        conn.execute('clear ip bgp * soft out')
        
    else:
        RED = '\033[31m'
        print(RED + "\nWARNING: \tPLEASE INPUT A CORRECT TASK AND IP ADDRESS!")
        print(f"NOTE:\t\tNO CHANGES HAS BEEN MADE!")
        print(Style.RESET_ALL)
        

# Read input data.
accounts = get_accounts_from_file('/root/crash_course/project/accounts.cfg')
hosts = get_hosts_from_file('/root/crash_course/project/hostlist.txt',default_protocol='ssh2')

queue = Queue(max_threads=5)
queue.add_account(accounts)
queue.run(hosts, do_something,)
queue.shutdown()                
