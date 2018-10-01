import pika
credentials = pika.PlainCredentials('guoqi', '1')
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",
                                                               port=5672,
                                                               virtual_host="t",
                                                               credentials=credentials))
