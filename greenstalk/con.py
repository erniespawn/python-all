import beanstalkc

beanstalk = beanstalkc.Connection(host='localhost', port=11300)

while True:
  job = beanstalk.reserve(b'')
  #Job should be processed here or in another function
  job.delete()
