spiders
===

python scrapy
---
* douban

use django with scrapy
---

安装
---
    pip install -r requirements.txt

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

### 准备事项
    假设项目在 ~/python/spiders 下

    1. 由于配置文件里面有data, log这两个文件夹
       在有scrapy.cfg文件的目录(~/python/spiders/tutorial)
       建立 data, log文件夹

    2. settings里面默认将django的路径写死sys.path.insert(0, '/opt/spider_django')
       所以需要将spider_django加到/opt下
       sudo ln -s ~/python/spiders/tutorial/spider_django /opt

    3. ~/python/spiders/tutorial/spider_django 下找到manage.py
       python manage.py syncdb

