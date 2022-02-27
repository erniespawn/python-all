#!/usr/bin/env python
import greenstalk
import json
import sys
import random

beanstalkTube = 'YouTube'
beanstalkHost = 'localhost'
beanstalkPort = 11300

client = greenstalk.Client((beanstalkHost, beanstalkPort))
client.use(beanstalkTube)

while(True):

    client.put('message {}'.format(random.randint(100,190)))

