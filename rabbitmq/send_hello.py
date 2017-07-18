#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='reindeer.rmq.cloudamqp.com'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='hello rabbitmq!')
print("[x]send 'hello rabbitmq!'")
connection.close()

