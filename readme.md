# 安装步骤
1. 配置数据库
2. 迁移数据库
```
python manage.py makemigrations
python manage.py migrate
```
3. 创建管理员
```
python manage.py createsuperuser
```
4. 启动
```
python manage.py runserver
```



# vs code 远程连接
```
screen -r django
# django 运行终端
```