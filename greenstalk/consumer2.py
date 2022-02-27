#!/usr/bin/env python
import greenstalk
import json
import sys

beanstalkTube = 'Kenny-tube'
beanstalkHost = 'localhost'
beanstalkPort = 11300

client = greenstalk.Client((beanstalkHost, beanstalkPort))
client.use(beanstalkTube)

while(True):
    job = client.reserve()

    print(job.body)


