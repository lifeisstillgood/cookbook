
## Setting up emacs home directory
## add a elisp dir to store all the .el files I want

ELISPDIR=~/elisp
MAKEFILE=$ELISPDIR/Makefile
mkdir $ELISPDIR

echo "## pbrian emacs elisp make file after http://edward.oconnor.cx/2005/09/installing-elisp-files" > $MAKEFILE
echo "sqlmode.el:" >> $MAKEFILE
echo "    git clone http://repo.or.cz/w/emacs.git/blob/HEAD:/lisp/progmodes/sql.el " >> $MAKEFILE






