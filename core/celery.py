import os
from celery import Celery
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.autodiscover_tasks(['investdata'])

app.conf.beat_schedule = {
    "fetch-stocks-every-minute": {
        "task": "investdata.tasks.fetch_all_stocks_task",
        "schedule": timedelta(minutes=1),  # a cada 1 minuto
    },
}