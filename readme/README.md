# 1 . Python安装和Django项目本地启动

## 1.1 首先安装Python3

- 下载

  链接 https://www.python.org/downloads/windows/，太新的没用过，不知道有什么新的特性；这里选择3.7的就行，https://www.python.org/ftp/python/3.7.7/python-3.7.7.exe 选择windows可执行文件下载。

- 安装

  安装基本除了选择安装目录，其他的直接下一步即可

- 配置环境变量

  安装的时候理论上会有选择添加环境变量，如果没有的话，需要自行配置，这里不再赘述

- 更换pip国内源

  - windows环境
  ```
  # 在你的用户目录下新建pip目录
  C:\Users\Administrator\pip
  
  # 进入pip目录新建pip.ini文件，文件内容如下:
  
  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  [install]
  trusted-host = https://pypi.tuna.tsinghua.edu.cn  
  # trusted-host 此参数是为了避免麻烦，否则使用的时候可能会提示不受信任
  ```
  
  - linux环境
  ```
  mkdir ~/.pip 
  vi ~/.pip/pip.conf，文件内容如下:
  
  [global] 
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  [install]
  trusted-host = https://pypi.tuna.tsinghua.edu.cn
  
  ```
  
- 验证你的Python环境

  ```
  # 如果只安装了Python3，默认Python 就指向Python3
  # 进入cmd,输入下面的命令
  C:\Users\Administrator>python -V
  Python 3.7.6
  
  C:\Users\Administrator>pip -V
  pip 19.2.3 from d:\programs\python37\lib\site-packages\pip (python 3.7)
  
  ```

  

## 1.2 下载*PyCharm*专业版并破解

- 直接官网下载

  下载链接https://download.jetbrains.com/python/pycharm-professional-2019.3.2.exe；

  最近的破解不一定适用，暂时下的稍微老一点的版本

- 破解(这个破解包能支持破解Jetbrains家全部产品)

  链接: https://pan.baidu.com/s/1tNY52nv7pFRZ_5_WDOnDTw 提取码: xmrk

  （直接把`jetbrains-agent-latest.zip`拖进IDE就行了，然后重启*PyCharm*即可）



## 1.3 启动调试Django项目

- 打开PyCharm,导入项目

  假定你的pycharm工作目录是``E:\PycharmProjects\`` ,把blog项目解压到该目录

  ![](..\readme\assets\1589473744302.png)

导入blog项目

- 新建虚拟环境

按下图指示选择你的Python3的安装目录为基础，新建一个虚拟环境

![](..\readme\assets\1589474161194.png)

  ![](..\readme\assets\20200515_0043082020515048472.gif)

以上gif中，我都已经有虚拟环境了，只做演示

- 启动django项目

  - 修改setting文件中的mysql连接

    ![1589508912029](..\readme\assets\1589508912029.png)

  -   生成迁移文件

    `` python manage.py makemigrations``

  -  执行迁移生成表

    ``python manage.py migrate``

  -  注册后台管理员

    `` python manage.py createsuperuser``

  -  启动服务

    `` python manage.py runserver （默认端口是8000）``

- 修改’‘我’‘的痕迹

  以上步骤理论上来说都是为这一步做准备的，想要真正使用本项目建站，就要去除网页中’我‘的痕迹，快捷键Crtl+Shift+R 直接全文替换，如图所示：

   ![1589536353071](..\readme\assets\1589536353071.png)

# 2. django-docker项目说明

- 使用docker-compose部署：django2.0+nginx+uwsgi+mysql

  
## 1.1 安装docker & docker-compose
- docker安装使用: <http://sunyune.com/article/docker1/>
- docker-compose安装使用: 

## 1.2 快速使用
```bash
$  git clone 
$  docker-compose up -d        # 启动所有容器
$  docker-compose down         # 关闭所有容器
启动后访问：http://47.94.166.230
```

## 1.3 如果使用前后端不分离的项目需要收集Static Files给nginx访问
```bash
$ docker-compose exec web bash
$ python manage.py collectstatic 
```

## 2.1 说明
### 2.1.1 设置项目访问的服务DNS解析

```python
[root@linux-node1 web]# vim /etc/hosts
192.168.56.1 mysql
192.168.56.11 redis
```

### 2.1.2 配置mysql账号和密码

```python
# 1、创建用户
create user 'django'@'%' identified by 'django';
create database djangodocker charset utf8;

# 2、授予mup用户授予对mup数据库的操作权限
GRANT ALL ON djangodocker.* TO 'django'@'%';
flush privileges;
select host,user from mysql.user;
```

### 2.1.3 安装依赖包
```python
[root@linux-node1 django-docker]# yum install mysql-devel  # 安装mysl-dev避免安装mysqlclient报错
[root@linux-node1 django-docker]# pip3 install -r requirements.txt 
```

### 2.1.4 启动项目

```python
[root@linux-node1 web]#  cd /code/django-docker/web
[root@linux-node1 web]#  celery -A web worker -l info
[root@linux-node1 web]#  python3 manage.py runserver 0.0.0.0:8000
http://192.168.56.11:8000/
```