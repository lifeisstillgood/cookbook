

Set up a remote private git repo...
::

  ssh onto yur remote server paul-brian.com
  $ mkdir private.git
  $ cd private.git
  $ git init --bare

  we have now created a bare git repo.  This will by convention be the central
  point for our various different users (basically lots of my machines...)

Now create locally 

  $ mkdir private
  $ cd private
  $ echo foo > bar.txt
  $ git init
  $ git commit ... etc

  git remote add origin ssh://pbrian@paul-brian.com/home/pbrian/private.git

  git push origin master

  now the remote server paul-brian has a private repo on it, and I can clone and use it to share


  
