from celery import Celery
from .models import Page,Page_status_history
import requests

app = Celery('task',broker='http://127.0.0.1:7000/')
@app.task(name = "send notification")
def send_notification():
    x = Page.objects.get(name = 'xware main page') 
     
    response = requests.get('https://xware.co/') 
    Page_status_history.objects.create(Page = x,status_code_type = response.status_code,
    response_time = 54
    )
    