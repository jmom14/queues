from celery import Celery

celery_app = Celery("tasks", backend="rpc://", broker="pyamqp://guest@rabbitmq//")


@celery_app.task()
def add(a, b):
    for i in range(a, b):
        print(i)
    return {"number": a + b}
