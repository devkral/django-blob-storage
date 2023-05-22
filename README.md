# django-blob-storage

This is a fork from django-db-storage2

## Overview

Warning: In many cases, storing files in the database is a BAD idea. Your database will easily become bloated and the performance can degrade rapidly. See this `StackExchange post`\_ for more information.

.. \_StackExchange post: http://programmers.stackexchange.com/questions/150669/is-it-a-bad-practice-to-store-large-files-10-mb-in-a-database

This is a custom storage backend for storing files in the database instead of the file system and is a drop-in replacement for Django's FileSystemStorage. Some benefits of this application:

-   no changes needed to existing models, it just works (and if it doesn't, open a ticket!)
-   django-admin is implemented and can be used to search, upload, download and manage files
-   100% code coverage with unit tests
-   only db files need to be backed up

## Requirements

-   Python (3.5+)
-   Django (3.2+)

## Installation

Installation using pip::

    $ pip install django-blob-storage

Update `settings.py`

```python

    # Add 'dbstorage' to INSTALLED_APPS
    INSTALLED_APPS = [
        'dbstorage',
    ]

    # Optionally set DEFAULT_FILE_STORAGE
    DEFAULT_FILE_STORAGE = 'dbstorage.storage.DBStorage'

    # Optionally set  DJANGO_DBFILE_TRACK_ACCESSED=True to track accessed times

    # Choose a root url for uploaded files
    MEDIA_URL = '/media/'
```

Update `urls.py`

```python

    urlpatterns = [
        ...
        # dbstorage
        path("", include("dbstorage.urls")),
    ]
```

Run database migrations (done automatically, when included as app)

```sh

env DJANGO_SETTINGS_MODULE=tests.settings PYTHONPATH="." poetry run django-admin migrate


```

## How to Use

No modification are needed for models to work properly.

```python

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):

    file_field1 = models.FileField()
    file_field2 = models.FileField(upload_to='uploads/%Y/%m/%d/')
    file_field3 = models.FileField(upload_to=user_directory_path)
```

## Bugs?

Create an issue at https://github.com/devkral/django-blob-storage/issues
