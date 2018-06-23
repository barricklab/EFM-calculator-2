# Django Setup for Development

The EFM-Calculator-2 repository is structured like a Django app. This 
document explain how to set things up so that you can boot up a Django test 
server on your local machine for EFM-Calculator-2 development.

Create a directory that will include all of our development files and clone the 
GitHub repository into it:
```console
$ mkdir efm2dev
$ cd efm2dev
$ git clone https://github.com/barricklab/EFM-calculator-2.git
$ mv EFM-calculator-2 efm2
````
Notice that we renamed the repository directoy to efm2. This doesn't affect GitHub tracking,
but it is important for the directory structure of the Django server.

Create python virtual environment and install required modules into it. You must
use Python3 for the command that created the virtual environment. (Python3.6 was used 
when testing these instructions).

```console
$ python3 -m venv venv
$ source venv/bin/activate 
$ pip install -r efm2/requirements.txt
```
Note: If you add any required modules during development, you must add them to the `requirements.txt` file.

Create the Django site. Then move the efm2 repository to the location expected for a Django App.

```console
$ django-admin startproject efm2site
$ mv efm2 efm2site
$ cd efm2site
```

Connect the site to efm2 Django app .

1. Add 'efm2' to the `INSTALLED_APPS` list in `efm2site/settings.py`:

Your edited file should look like this:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'efm2',
]
```

2. Edit the file `efm2site/urls.py` to add an import of `include` from `django.urls` and add a line that includes the efm2 urls.

Your edited file should look like this:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('efm2/', include('efm2.urls')),
    path('admin/', admin.site.urls),
]
```

Start Django server:
```console
$ python manage.py runserver
```

To view the EFM Calculator webpage, use this URL:
http://127.0.0.1:8000/efm2/
