# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pika


class Base(object):
    def __init__(self, user, pwd, host, exchange=None, exchange_type=None):
        credentials = pika.PlainCredentials(user, pwd)
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host, credentials=credentials))  # 连接
        self.ch = self.conn.channel()  # 频道
        self.exchange = exchange
        if exchange and exchange_type:
            self.ch.exchange_declare(exchange=exchange, exchange_type=exchange_type)

    def send_task_fanout(self, body):
        if self.exchange:
            self.ch.basic_publish(exchange=self.exchange, routing_key='',
                                  properties=pika.BasicProperties(delivery_mode=2),
                                  body=body)

    def __del__(self):
        try:
            self.ch.close()
            self.conn.close()
        except Exception:
            pass


class Customer(Base):
    def __init__(self, user, pwd, host, task_queue, *store_queues, exchange=None, exchange_type=None, prefetch_count=1,
                 durable=True, no_ack=False):
        super().__init__(user, pwd, host, exchange=exchange, exchange_type=exchange_type)
        self.task_queue = task_queue
        self.store_queues = store_queues
        self.prefetch_count = prefetch_count  # 在同一时刻，不要发送超过x条消息给一个工作者（worker）
        self.durable = durable  # 队列声明为持久化
        self.no_ack = no_ack  # 消息响应 true为关闭
        self.exchange = exchange
        self.exchange_type = exchange_type

    def send_task(self, body):
        self.ch.basic_publish(exchange='', routing_key=self.task_queue,
                              properties=pika.BasicProperties(delivery_mode=2), body=body)

    def store_data(self, data, rk=None):
        routing_key = rk if rk else self.store_queues[0]
        self.ch.basic_publish(exchange='', routing_key=routing_key,
                              properties=pika.BasicProperties(delivery_mode=2), body=data)

    def server_forever(self, func):
        if self.task_queue is not None:
            self.ch.queue_declare(queue=self.task_queue, durable=self.durable)
            if self.exchange and self.exchange_type:
                self.ch.queue_bind(exchange=self.exchange, queue=self.task_queue)
        if self.store_queues:
            for sq in self.store_queues:
                if sq:
                    self.ch.queue_declare(queue=sq, durable=self.durable)

        self.ch.basic_qos(prefetch_count=self.prefetch_count)
        self.ch.basic_consume(func, queue=self.task_queue, no_ack=self.no_ack)
        self.ch.start_consuming()


class Producer(Base):
    def __init__(self, user, pwd, host, task_queue=None, durable=True, exchange=None, exchange_type=None):
        super().__init__(user, pwd, host, exchange=exchange, exchange_type=exchange_type)
        self.task_queue = task_queue
        self.durable = durable  # 持久化
        self.exchange = exchange

    def send_task(self, body):
        self.ch.basic_publish(exchange='', routing_key=self.task_queue,
                              properties=pika.BasicProperties(delivery_mode=2),  # make message persistent
                              body=body)
        # self.ch.close()

    def produce(self, func):
        if self.task_queue is not None:
            self.ch.queue_declare(queue=self.task_queue, durable=self.durable)
        func(self)
