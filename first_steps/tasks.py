#!/usr/bin/env

from celery import Celery

#app = Celery('tasks', broker='amqp://guest@localhost//')
app = Celery('tasks', broker='amqp://', backend='rpc://')

@app.task
def add(x, y):
	return x + y

