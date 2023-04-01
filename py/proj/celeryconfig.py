AMQP_URL = "amqp://admin:admin@localhost:5672"
REDIS_URL = "redis://:admin_password@localhost:6379/0"

broker_url = REDIS_URL
result_backend = REDIS_URL

include = ["proj.tasks"]

task_acks_late = True
task_serializer = 'json'
result_expires = 3600
result_serializer = 'json'
worker_prefetch_multiplier=1
worker_concurrency=1

accept_content = ['json']
enable_utc = True
