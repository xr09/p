P
=

Pragmatic service manager for impatient programmers.


Tired of those 'sudo service postgresql restart'?

How about 'sudo /etc/init.d/memcached restart'?

And the new kid in town: 'systemctl restart libvirtd'

Wouldn't be awesome to be able to type something like this?

    p pos 1      # start
    p mem 0      # stop
    p virt        # restart

And yes, mys is mysql, pos is postgres and mem is memcached, but you could also 
have typed ysql, ostgre, or mcache, yes! P uses some RegEx Fu to make
your life a lot simpler.

You only have to type any string contained in the name of the service you want
to change, 'pos' is ok for 'postgresql' as long as there are no more services whose
names contains 'pos'.

To start, stop or restart it uses numbers:

    stop    ->  0
    start   ->  1
    restart ->  2 (default, can be omitted) 

Todo List:

* Define service groups (web: mysql, memcached, lighttpd), then "p web 0".
* Detect init system and interact transparently with all of them.
