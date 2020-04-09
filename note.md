python manage.py startapp appName 创建新应用
python manage.py runsrever
sqlite3
轻量级嵌入式级的数据库，常规操作绝大多数和MySQL相同
设置页面语言，在setting.py的LANGUAGE_CODE = 'zh-hans'
python manage.py makemigrations创建初始的database
python manage.py migrate进行迁移
在urls.py 里面写路由
from django.conf.urls import url
万能键：alt + enter
实现一个请求，首先在urls中注册一个路由
##实现一个请求
- 注册一个路由
    - urls中
        - url
            - 参数1 正则表达式
        - 视图函数
            - 对应的是views中的一个函数
                - 没有括号
- 在views中实现对应的视图函数
    - 第一个参数是request
    - 永远记得返回response
    