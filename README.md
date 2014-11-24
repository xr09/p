p
=

Pragmatic service manager for impatient programmers.


Tired of those 'sudo service postgresql restart'?

How about 'sudo /etc/init.d/memcached restart'?

Wouldn't be awesome to be able to type something like this?

    p my 1      # start
    p po 0      # stop
    p me        # restart

And yes, my is mysql, po is postgres, li is lighttpd and me is memcahed.

You only have to type the starting characters of the service you want to change,
'po' is ok for 'postgresql' as long as there are no more services whose names
starts with 'po'.

start   ->  1,u
stop    ->  0,d
force-reload ->  fr,rl
restart ->  anything else

Right now it only recognizes a few services, the ones I use the most, 
but my goal is to read al available services and match against the string
you enter with regex, so postgresql could become psql, mysql could be typed
as mql and nginx as ngx.

Todo List:

* Apply changes to a list of services on the fly: "p lig,mem,my 1"
* Define service groups (web: mysql, memcached, lighttpd), then "p web 0"
* Match services with regular expressions "p ngx 6"


