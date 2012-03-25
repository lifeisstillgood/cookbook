#!/usr/local/bin/python
#! -*- coding: utf-8 -*-

import os

import myprocesslib
'''
:author: paul@mikadosoftware.com
:aim: To create a set of examples demonstrating a subversion session and use of ciotools.scrumtools

create: SVNOutputWrapper
create: 

1. Scrumtools supplies a cmd runner
   supplies a set of error handlers, and oo for SVN

2. build example SVN session with conflicts and branching
  
3. Run the example, manually handling exceptions

4. automate the running


Creating an example SVN session so I can demonstrate ScrumTools

1. create two developers working copies
2. show a conflict between two developers
3. show conflict between two changesets when merging into branch
4. show use of blame -g to see who really checked in things


initial setup
-------------
I have two sh files - just write out and run these.
They create two wc (A and B) and a qa branch

Then I want to diverge the A and B branches, and check in conflicting changes


B puts in honey
A puts in peasnut butter
A check in fails with conflict
A resolves in favour of peanut butter
TKT is fixed
B needs to add peanut butter and jelly - so resolves conflict in his favour
TKT2 is fixed

I merge in tkt1
then tkt 2 - will I get a conflict?

also a bad merge resolution - show honey example

'''

#### principles 
# cannot svn ci unless wc is upto HEAD/
# this is reasonable -its all about changesets

# can I do something like bisect - on a merge up failure, what chgsets between RC HEAD and uprev touch that file - extract those diffs?

workfolder="/usr/home/pbrian/samlearning.com/trac/merge/demo"
wcA=workfolder + "/arnie-wc"
wcB=workfolder + "/bertie-wc"

config = """

## constants
export workfolder=%s
export myrepo=$workfolder/demo_repo
export myrepoURL=file://$myrepo
export proj=/tmp/mycafe
### working copies 
wcA=%s
wcB=%s
""" % (workfolder, wcA, wcB)

setup = """
cd %s
. config.sh

### clean down
rm -rf $myrepo
rm -rf $wcA
rm -rf $wcB

###                        set up a svn repository 

mkdir $myrepo
svnadmin create $myrepo

###  initialise the repo for a Cafe Project

mkdir -p $proj/trunk
mkdir -p $proj/branches
mkdir -p $proj/tags

echo bread >> $proj/trunk/menu.txt
echo ham >> $proj/trunk/menu.txt
echo bread >> $proj/trunk/menu.txt

svn import $proj $myrepoURL -m 'initial import'

### we can remove the tmp setup 
rm -rf $proj


### Now create two develoers machines
mkdir $wcA $wcB
svn co $myrepoURL $wcA
svn co $myrepoURL $wcB


#####                                   Now for fun


############################################ ci 4 - make QA branch                                                            
cd $wcA/
echo make QA
svn cp $myrepoURL/trunk $myrepoURL/branches/qa -m 'making branch for QA testing'
svn up


cd $wcA/branches/qa
svnmerge.py init
svnmerge.py integrated
svn propget svnmerge-integrated
echo ci6
svn ci -m 'svnmerge now owns QA branch'
########################################### 

"""  % workfolder

peanut1 = """bread
peanut butter
bread"""

honey1 = """bread
honey
bread"""

peanut2 = """bread
peanut butter
jam
bread"""


#write out to wca the change
#main idea is to get bPB > BHB in repo, then BPJB in local and svn up - get BHJB.
##need to turn off svn mergeinfo - no smart merges?

#setup
open(os.path.join(workfolder, 'setup.sh'),'wb').write(setup)
open(os.path.join(workfolder, 'config.sh'),'wb').write(config)
open(os.path.join(workfolder, 'peanut1'),'wb').write(peanut1)
open(os.path.join(workfolder, 'peanut2'),'wb').write(peanut2)
open(os.path.join(workfolder, 'honey1'),'wb').write(honey1)



print myprocesslib.runcmd(['/bin/sh', os.path.join(workfolder, 'setup.sh') ])

open(os.path.join(wcA, "trunk/menu.txt"),'w').write(peanut1)
print myprocesslib.runcmd(['svn', 'ci', wcA, '-m', 'peanut1'])

open(os.path.join(wcB, "trunk/menu.txt"),'w').write(honey1)
try:
    print myprocesslib.runcmd(['svn', 'ci', wcB, '-m', 'honey1'])
except myprocesslib.MikadoSVNMergeError, e:
    print e

print """
### this check in fails - it fails becaue the merging is done on local copy all the time
### this then means that the local copy sends up a change that was made against an out of date menu/
### so we need to run update
"""
print myprocesslib.runcmd(['svn', 'up', '--accept', 'postpone', wcB])
print myprocesslib.runcmd(['cat', os.path.join(wcB, "trunk/menu.txt")])
open(os.path.join(wcB, "trunk/menu.txt"),'w').write(honey1)
print myprocesslib.runcmd(['cat', os.path.join(wcB, "trunk/menu.txt")])

## even though I have resolvd the conflict, SVN still has that file marked as conflicted, so it would refuse to work unless
print myprocesslib.runcmd(['svn', 'resolved', os.path.join(wcB, "trunk/menu.txt")])
print myprocesslib.runcmd(['svn', 'ci', wcB, '-m', 'honey1'])

open(os.path.join(wcA, "trunk/menu.txt"),'w').write(peanut2)
print myprocesslib.runcmd(['svn', 'up', wcA ])

print """ At this point SVN has merged two files - it thinks successfully
However if Arnie looks at his menu file, it is not what he just wrote in his file,
and unless he is careful it will sit there

however the resultant file is totally unknown to anyone - no developer ever put that file together.

Is this correct? Is it bad merging practise?


I think so, yes.
Files should not change underneath a developer...
THe correct way to approach this is the developer to work in their own branch
then merge changes into - however that is what is happening 

But why the bad merge ...
 """

print myprocesslib.runcmd(['cat', os.path.join(wcA, "trunk/menu.txt")])

### now force a conflict ...

print myprocesslib.runcmd(['svn', 'ci', wcA, '-m', 'mixed1'])
open(os.path.join(wcA, "trunk/menu.txt"),'w').write(peanut2)
print myprocesslib.runcmd(['svn', 'up', '--accept', 'postpone', wcA ])
