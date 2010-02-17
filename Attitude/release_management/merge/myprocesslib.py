#! /usr/local/bin/python
#! -*- coding:utf-8 -*-

"""
Library function(s) for ScrumStuff

combine this with mikadoSVNLib 



revert: merge -r 100:99

from 100 back to 99


A defined example workflow with checkins, conflicts and so on.



"""

import subprocess
import os



class MikadoSVNMergeError(Exception):
    ''' '''
    pass

class MikadoCmdLineError(Exception):
    ''' '''
    pass



def runcmd(cmdlist):
    '''given a cmd in list form, execute it in subprocess.Popen

    Designed for handling svnmerge issues '''

    print "Running ...", ' '.join(cmdlist)
    p = subprocess.Popen(cmdlist, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output, err = p.communicate()
    except Exception, e:
        raise MikadoCmdLineError(str(e))

    if err:
        raise MikadoSVNMergeError(err)
    else:
        return output

#use byt catchin evnmerge error then dealing with conflict

## issues - the ci txt file is output local to here...
if __name__ == '__main__':

    sourcePath = '/usr/home/pbrian/samlearning.com/merge/arnie-wc/trunk'
    destPath = '/usr/home/pbrian/samlearning.com/merge/arnie-wc/branches/qa'
    cmd = ['python', '/usr/local/bin/svnmerge.py', 'merge', '-r', '8', '--source', sourcePath, destPath]
    pwd = os.getcwd()

    successCI = ['svn', 'ci', destPath, '-F', os.path.join(pwd, 'svnmerge-commit-message.txt')]

    try:
        output = runcmd(cmd)
        if output == '':
            print "No changes in this rev can be merged"
        else:

            print "Success ++++", output, "++++"
            print ' '.join(successCI)

    except MikadoSVNMergeError, e:
        print "WHoops - check for conflicts", e


