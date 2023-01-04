from .models import category
import random
import requests
from .models import Page
from .models import Page_status_history
def my_scheduled_job():
    # number = random.randint(0,100)
    # category.objects.create(category_name = number)
    
    x = Page.objects.get(name = 'xware main page') 
     
    response = requests.get('https://xware.co/') 
    Page_status_history.objects.create(Page = x,status_code_type = response.status_code,
    response_time = 54
    )
    