from Exscript.util.start import quickstart
from Exscript.util.file import get_hosts_from_file, get_accounts_from_file
from Exscript import Account

command = input("enter command: ")

def do_something(job, host, conn):
    conn.execute('term len 0')
    conn.execute(command)
    
accounts = get_accounts_from_file('accounts.cfg')
hosts = get_hosts_from_file('hostlist.txt',default_protocol='ssh2')
quickstart(hosts, do_something, max_threads=15,verbose=1)