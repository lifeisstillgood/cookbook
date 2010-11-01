
cd /usr/home/pbrian/samlearning.com/trac/merge/demo
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

