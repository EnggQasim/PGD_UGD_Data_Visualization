# Django (MVC)
* Model->table and databases
* view -> web pages display functions logic
* controls -> urls, table of contents

## Vritual Envornment
* `python -m venv <name>`
    * activate in window
        * `.\<name>\Scripts\activate`
    * activate in linux
        * `source <name>/bin/activate`
* install pacakages
    * `pip install django numpy pandas`
* pip freeze
    * `pip freeze` show all packages in current active envornment
    * `pip freeze > requirments.txt` all current packages name write in **requirments.txt
    * `pip install -r requirments.txt` install all packages from **requirements.txt** file
## Start working on Django
* check django version `python -m django --version`
* Now create new project name **p1** `django-admin startproject <name>`
* run django project server -> move terminal into your **project directory**`
    * `cd <projectfolder>`
    * `python manage.py runserver`

### Create new application in current project
`python manage.py startapp <polls>`
* create new file in **<polls>/urls.py**
```
from django.urls import path
from . import views # import views.py file here

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about,  name='about')
]
```
* **<polls>/views.py**

```
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("<h1>Pakistan zinda bad</h1>")
```

* now got into **p1/urls.py**
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("polls/", include('polls.urls')),
    path('admin/', admin.site.urls),
]
```