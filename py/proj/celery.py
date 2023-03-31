from celery import Celery

AMQP_URL = "amqp://admin:admin@localhost:5672"
REDIS_URL = "redis://:admin_password@localhost:6379/0"
BROKER_URL = REDIS_URL

app = Celery("proj", broker=BROKER_URL, include=["proj.tasks"])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    worker_concurrency=1,
)

if __name__ == "__main__":
    app.start()
