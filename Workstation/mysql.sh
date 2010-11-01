mkdir /var/db/mysql
chown -R mysql:mysql /var/db/mysql/


mysql_datadir=/usr/local/var/db/mysql
mkdir -p $mysql_datadir
chown mysql:mysql $mysql_datadir
/usr/local/bin/mysql_install_db --user=mysql --datadir=$mysql_datadir

#start up mysql manually.
#NB mysqld_safe is a script that runs the real binary
#(/usr/local/libexec/mysqld) and restarts it if needed
cd /usr/local
/usr/local/bin/mysqld_safe &

