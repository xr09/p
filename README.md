p
=

Pragmatic service manager for impatient programmers.


Tired of those 'sudo service postgresql restart'?

How about 'sudo /etc/init.d/memcached restart'?

Wouldn't be awesome to be able to type something like this?

    p my 1      # start
    p po 0      # stop
    p lig fr    # force reload
    p me 6      # restart

And yes, my is mysql, po is postgres, lig is lighttpd and me is memcahed.

Right now it only recognizes a few services, the ones I use the most, 
but my goal is to read al available services and match against the string you enter with regex,
so postgresql could become psql, mysql could be typed as mql and nginx as ngx.

How cool is that?


