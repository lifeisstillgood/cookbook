
. config.sh

mark=++++

#QA branch is made from ci 1 

#### arnie likes cheese.
echo "$mark Arnie replaces ham with cheese"
cp $workfolder/_cheese $wcA/trunk/menu.txt
echo "$mark Arnie checks it in"
svn ci $wcA/trunk -m 'Arnie likes cheese'


echo "$mark Bertie goes for salmon "
cd $wcB
cat $wcB/trunk/menu.txt | sed s/ham/salmon/ > /tmp/foo.txt; mv /tmp/foo.txt $wcB/trunk/menu.txt
cat $wcB/trunk/menu.txt
### ci4 salmon (fails)
svn ci $wcB/trunk/menu.txt -m 'Bertie chooses salmon'
echo "$mark We can see that to check into trunk the wc needs to be up to date. obviously"

cd $wcB
svn up --accept 'mine-conflict' #be quite rude
cat $wcB/trunk/menu.txt
svn ci $wcB/trunk/menu.txt -m 'Bertie chooses salmon - second try'
cat $wcB/trunk/menu.txt




##### OK
##
# I want to create a realistic scenario
# One dev checks in good code to trunk, one bad, mixed up
# We want to pull the chgsets that are good and apply up, then
# alter slightly, then back down and also up to RC (?)
#
#
#
#####


#### make a change that is 'good'
cd $wcA/
svn up --accept 'mine-conflict' #be quite rude
cp ../_cheesetomato ./trunk/menu.txt
cp ../_chips ./trunk/chips.txt

echo $mark add chips
svn add ./trunk/chips.txt
svn ci -m 'cheese on toast + chips - yummy $wcA'

#### make a change that is 'good'                                                                                             
cd $wcB/
svn up --accept 'theirs-conflict' #be quite rude
cp ../_spam ./trunk/menu.txt
cp ../_chipsthin ./trunk/chips.txt
echo "crap" > ./trunk/crap.txt
svn add ./trunk/crap.txt
echo $mark CI... bad food
svn ci -m 'spam and thin chips $wcB'

cd $wcA/
svn up --accept 'mine-conflict' #be quite rude
cp ../_cheesetomato ./trunk/menu.txt
cp ../_chipsthick ./trunk/chips.txt      
#just checking we did remove the crap file
svn del ./trunk/crap.txt
echo $mark CI... good food                 
svn ci -m 'cheesetom and thick chips $wcA'



### but the diff between 3 and 5 and 3 and 6 arer different
cd $wcA/branches/qa
svnmerge.py integrated

svnmerge.py merge -n -r1:8

this seems to be the key - merge from R to R - so the middle conflicts are essentially avoided by doing a fast forward merge
The conflicts were resolved at each step of the way.

Can we envsage a two stage problem - not really.
We are always walking from last known good changeset. So any checkins through the changesets will be followed, then discarded.
use a python wrapper - do the commits, and subprocess, and then see if anything fails...

commiting back down, and QA to RC ...



