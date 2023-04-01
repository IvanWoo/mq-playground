from time import sleep

from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task(autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 5})
def slow_add(x, y):
    sleep(10)
    return add(x, y)
