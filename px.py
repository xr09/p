#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  px.py
#
#  Copyright 2013 Manuel E. Gutierrez <xr09 at github>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


import sys
import os

#~ SERVICES = os.listdir('/etc/init.d/')


SERVICES = ['lighttpd', 'memcached', 'postgresql', 'mysql',
            'prosody', 'ssh', 'wicd', 'hostapd', 'udhcpd']

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

