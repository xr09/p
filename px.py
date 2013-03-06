#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Manuel E. Gutierrez <xr09.github.com>
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

SERVICES = ['lighttpd', 'memcached', 'postgresql', 'mysql',
            'prosody', 'ssh', 'wicd', 'hostapd', 'udhcpd', 'dnsmasq']

def main():
    if len(sys.argv) >= 2:
        service_to_call = []
        action_to_do = None
        for service in SERVICES:
            if service.startswith(sys.argv[1]):
                service_to_call.append(service)
        if len(sys.argv) == 3:
            action_to_do = sys.argv[2]
        if not service_to_call:
            print('no matches')
        elif len(service_to_call) == 1:
            print(service_to_call[0])
            #~ print(action_to_do)
            if action_to_do in ['0', 'd']:
                action = 'stop'
            elif action_to_do in ['1', 'u']:
                action = 'start'
            elif action_to_do in ['fr', 'rl']:
                action = 'force-reload'
            else:
                action = 'restart'
            print(action)
            os.system("sudo service %s %s" % (service_to_call[0], action))
            return
        else:
            print('to many matches')
            for i,s in enumerate(service_to_call):
                print "%i -> %s" % (i+1, s)
        return 0
    print 'wrong args'
    return 1

if __name__ == '__main__':
    main()

