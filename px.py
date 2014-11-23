#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Manuel E. Gutierrez <mgp@nauta.cu>
#
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import sys
import os
import re


VERSION = '0.2'

# Default service  list
# Just in case there is no /etc/p.conf
DEFAULT_SERVICES = "memcached ssh postgresql mysql prosody wicd hostapd \
            udhcpd dnsmasq apache2 httpd nginx networking php5-fpm uwsgi gunicorn preload \
            ferm libvirtd".split()

# read service groups form .p.conf
SERVICE_GROUPS = {'web': 'nginx php5-fpm', 'db': 'postgresql memcached'}


def detect_service(name_to_match):
    """ Match input string against system services.
    Pick the best match.

    @param name_to_match: input string
    @return service: detected service name
    """
    pattern = re.compile('.*{0}.*'.format(name_to_match), re.IGNORECASE)
    #~ matched = []
    #~ for service in DEFAULT_SERVICES:
        #~ if pattern.match(service):
            #~ matched.append(service)
    return [ service for service in DEFAULT_SERVICES if pattern.match(service)]
    #~ if len(matched) == 1:
        #~ return matched[0]
    #~ else:
        #~ return None


def print_help():
    """ Print basic usage"""
    USAGE = """P (as in Pragmatic)

version: {0}

P is a simple frontend for managing init systems. No more dealing with 'service', 'systemctl' or '/etc/init.d/', just use p and take advantage of its regex support.

Starting a service: (p regex 1)
    p mysq 1      # start mysql

Stoping a service: (p regex 0)
    p pos 0      # stop postgres

Restarting a service: (p regex)
    p libvi        # restart libvirtd

Remember you must type enough characters to avoid name collisions.

The regex match in the code is like this: .*regex.*, so you can type
something like 'p emcach 1' and it still matchs 'memcached'.
""".format(VERSION)
    print(USAGE)



if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        service = detect_service(args[1])
        count = len(service)
        if count == 0:
            print("No service was matched with '%s'" % args[1])
        elif count == 1:
            print("do stuff to %s" % service)
        else:
            print("to many matchs: %s" % service)
    else:
        print_help()
