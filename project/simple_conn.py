#!/usr/bin/env python
from Exscript import Queue
from Exscript.util.log import log_to
from Exscript.util.decorator import autologin
from Exscript.util.file import get_hosts_from_file, get_accounts_from_file
from Exscript.util.report import status, summarize

print ('-' * 60)
print ("\t\tCLI BASE DDOS MITIGATION SCRIPT")
print ('-' * 60)
task = input("DIVERT/NO_DIVERT\t: ")
wildcard = '0.0.0.255 any'
command = input(f"\nIP BLOCK\t\t: ")

@autologin()



def do_something(job, host, conn):
    
    if task == 'DIVERT':
        conn.execute('term len 0')
        conn.execute('conf t')
        conn.execute('ip access-list extended NORMAL')
        conn.execute('no permit ip any any')
        conn.execute(f"deny ip {command} {wildcard}")
        conn.execute(f"permit ip any any")
        
        conn.execute('ip access-list extended DIVERT')
        conn.execute('no deny ip any any')
        conn.execute(f"permit ip {command} {wildcard}")
        conn.execute('deny ip any any')
        
    elif task == 'NO_DIVERT':
        conn.execute('term len 0')
        conn.execute('conf t')
        conn.execute('ip access-list extended NORMAL')
        conn.execute('no permit ip any any')
        conn.execute(f"no deny ip {command} {wildcard}")
        conn.execute(f"permit ip any any")
        
        conn.execute('ip access-list extended DIVERT')
        conn.execute('no deny ip any any')
        conn.execute(f"no permit ip {command} {wildcard}")
        conn.execute('deny ip any any')
        
    else:

        print(f"\nPLEASE SELECT A CORRECT OPTIONS!")
        print(f"NO CHANGES HAS BEEN MADE!!")

        

# Read input data.
accounts = get_accounts_from_file('accounts.cfg')
hosts = get_hosts_from_file('hostlist.txt',default_protocol='ssh2')

# Run do_something on each of the hosts. The given accounts are used
# round-robin. "verbose=0" instructs the queue to not generate any
# output on stdout.

queue = Queue(max_threads=5)
queue.add_account(accounts)     # Adds one or more accounts.
queue.run(hosts, do_something,) # Asynchronously enqueues all hosts.
queue.shutdown()                # Waits until all hosts are completed.


