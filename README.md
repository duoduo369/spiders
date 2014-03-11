spiders
===

python scrapy
---
* douban

use django with scrapy
---

http://stackoverflow.com/questions/19068308/access-django-models-with-scrapy-defining-path-to-django-project

### 1. 文件的目录结构如下，scrapy项目于django项目同级
    /home/rolando/projects
    ├── mybot
    │   ├── mybot
    │   │   ├── __init__.py
    │   │   ├── items.py
    │   │   ├── pipelines.py
    │   │   ├── settings.py
    │   │   └── spiders
    │   │       └── __init__.py
    │   └── scrapy.cfg
    └── myweb
        ├── manage.py
        ├── myapp
        │   ├── __init__.py
        │   ├── models.py
        │   ├── tests.py
        │   └── views.py
        └── myweb
            ├── __init__.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py

### 2.scrapy的setting中加入django的环境变量
    # Setting up django's project full path.
    import sys
    sys.path.insert(0, '/home/rolando/projects/myweb')

    # Setting up django's settings module name.
    # This module is located at /home/rolando/projects/myweb/myweb/settings.py.
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'myweb.settings'
