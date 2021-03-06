import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import webbrowser
import urllib2

# Get the keys from a specific url and then use them to connect to AWS Service 
#access_key_id = webbrowser.open('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key') 

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
res = response.read()
access_key_id = res[:20]
secret_access_key = res[21:]

print access_key_id
print secret_access_key

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)


queue_name = sys.argv[1]
# Get a list of the queues that exists and then print the list out
rs = conn.get_queue(queue_name)
# Get a list of the queues that exists and then print the list out
#rs = conn.get_all_queues()

rs.set_message_class(Message)		
m = Message()
m.set_body(sys.argv[2])
rs.write(m)

#conn.RawMessage(sys.argv[1], sys.argv[2])

#print 'message: %s has been written	to	the	queue' % sys.argv[2] 
