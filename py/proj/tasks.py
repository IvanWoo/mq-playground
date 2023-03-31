from .celery import app
from time import sleep


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def slow_add(x, y):
    sleep(10)
    return add(x, y)
