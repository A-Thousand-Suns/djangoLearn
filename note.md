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
    
##html
- ul>li*n + tab快捷生成
- 在views中渲染html文件（使用第二种）
    - 在App文件夹中操作
        - 在views中定义对应的函数，定义return时使用render(request, 'htmlname')
        - 在所在的App文件夹中新建templates文件夹，在其中新建对应的heml文件
        - 将templates 文件夹 mark the dictionary as template folder
        - 在settings文件中的INSTALLED_APPS添加该App文件夹
    - 在根目录下操作
        - 在根目录下新建templates文件夹并mark as template folder
        - 在该temlates文件夹下新建所需的html文件
        - 在views 文件中添加对应的函数
        - 在settings文件的TEMPLATES的'DIRS'中添加os.path.join(BASE_DIR, 'templates')

##路由分发
- 新建一个App 为Two, 在settings里将Two注册
- 在two中新建urls文件
- 在项目urls文件中添加url(r'^two/', include('Two.urls')),
##models 使用了ORM技术
- object relationshil mapping对象关系映射
- 将业务逻辑进行了解耦
    - objec.save()
    - object.delete()
- 关系型数据库
    - DDL
    - 通过model进行表的定义
    - 数据操作
        - 增删改查
        - 存储
            - save()
        - 查询
            - 查所有 Classname.objects.all()
            - 查单个 Classname.objects.get(args)
        - 查询
            - 需要基于查询
            - 查找到的对象修改属性之后save()
        - 删除
            - 基于查询
            - 查找到的对象使用delete()
      
    
##快捷键
- ctrl + p 参数提示