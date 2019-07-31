#!/usr/bin/env python
# -*- coding:utf-8 -*-
import traceback

from utils.log_manage import get_logger


class Scheduler:
    def __init__(self,customer,producer):
        self.customer = customer
        self.producer = producer
        self.logger = get_logger('schedule')
        self.dic_map = {

        }
    def get_task(self,):
        def callback(ch, method, properties, body):
            try:
                goods_id = pass
            except ImportError: #//TODO
                self.customer.send_task(body)
                self.logger.info('re send data to MQ')
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception:
                self.logger.error(body)
                self.logger.error(traceback.format_exc())
            else:
                ch.basic_ack(delivery_tag=method.delivery_tag)  # task done

        self.logger.info('start consuming!')
        self.customer.server_forever(callback)

    def get(self):
        return