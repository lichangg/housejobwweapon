#!/usr/bin/env python
# -*- coding:utf-8 -*-
import configparser

env='test'

parser = configparser.ConfigParser()
parser.read('config.ini',encoding='utf-8')


