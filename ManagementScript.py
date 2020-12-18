
import FortigateApi #this api library not belong to me but i changed a little bit for my create func.
import argparse
import sys

fg = FortigateApi.Fortigate('192.168.140.128', 'root', 'admin', 'password') #(firewall ip , virtual domain name, username,password)

class Manage(object):

    def __init__(self):
        
        parser = argparse.ArgumentParser(
            description='This script is going to manage your firewall remotely. "',
            usage=''' <command> [<args>]

Managing commands are:
   create     Create a rule
   list       Print a rule with id
   read       Printing all firewall rules.
   delete     delete rule with id
   update     update rule with id
''')
        parser.add_argument('command', help='Subcommand to run')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            #parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        
        getattr(self, args.command)()

    def create(self):    #func for creating fw policy
        parser = argparse.ArgumentParser(
            description='''Please Enter given params.
            srcintf='any', dstintf='any', srcaddr='all', dstaddr='all', service='ALL', action='accept', 
            # schedule='always',  status='enable' 
            ''')
        # prefixing the argument with -- means it's optional
        parser.add_argument('srcintf')
        parser.add_argument('dstintf')
        parser.add_argument('srcaddr')
        parser.add_argument('dstaddr')
        """parser.add_argument('service')
        parser.add_argument('action')
        parser.add_argument('schedule')
        parser.add_argument('status')
        parser.add_argument('name')"""

        args = parser.parse_args(sys.argv[2:])
        
        fg.AddFwPolicy(args.srcintf,args.dstintf,args.srcaddr,args.dstaddr)

    def update(self): # updating a rule with given id
        parser = argparse.ArgumentParser(
            description='''Update rule with given params.
            id=value , srcintf='any', dstintf='any', srcaddr='all', dstaddr='all', service='ALL', action='accept', 
            # schedule='always', nat='disable', poolname='[]', ippool='disable', 
            # status='enable', comments='', traffic_shaper='', traffic_shaper_reverse=''
            ''')
        # prefixing the argument with -- means it's optional
        parser.add_argument('id')
        parser.add_argument('srcintf')
        parser.add_argument('dstintf')
        parser.add_argument('srcaddr')
        parser.add_argument('dstaddr') 

        args = parser.parse_args(sys.argv[2:])
        fg.SetFwPolicy(args.id,args.srcintf,args.dstintf,args.srcaddr,args.dstaddr)    
        
    def list(self):  # list the all rules.
        fg.GetFwPolicyID('')
    
    def read(self): #reading spesific rule with given id
        parser = argparse.ArgumentParser(
            description='Read spesific rule with id')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('value')
        args = parser.parse_args(sys.argv[2:])
        fg.GetFwPolicyID(str(args.value))
    def delete(self): # deleting spesific rule with given id
        parser = argparse.ArgumentParser(
            description='delete spesific rule with id')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('value')
        args = parser.parse_args(sys.argv[2:])
        fg.DelFwPolicyID(str(args.value))


if __name__ == "__main__":
    Manage()

  
    
    

