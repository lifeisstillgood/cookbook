#!/usr/local/bin/python
#! -*- coding:utf-8 -*-

__doc__ = ''' '''


import md5
import sys
from getpass import getpass

def logit(domain, passwd, user):

    fo = open('passwords.txt','a')
    fo.write("\n%s:%s:%s" % (domain, passwd, user))
    fo.close()


def main():
    domain = sys.argv[1:][0]
    user, hex = run(domain)
    logit(domain, hex[:8], user)
    print "For domain: %s, user %s " %  (domain , user)
    print "use password: %s" % hex[:8]


def run(domain):

    m = md5.new()
    m.update(domain)

    user = raw_input("Enter username: [paul@mikadosoftware.com]: ")
    if user == '': user = "paul@mikadosoftware.com"
    pass_ = getpass("Enter generic passwd: ")

    m.update(pass_)
    
    return (user, m.hexdigest())
    
if __name__ == '__main__':
    main()
