# 回测系统使用指南（系统环境建议 Windows Server 2019 Datacenter）

## Windows系统

> **安装Anaconda**推荐

```
https://repo.continuum.io/archive/.winzip/ 
安装时注意将后面的添加为系统环境变量选项打勾

【推荐版本】
Anaconda3-2021.11-Windows-x86_64.zip	507.5M	2021-11-17 12:10:52 (Python 3.9.7)
```

> **安装依赖库**

```
点击【install.bat】安装
```

**安装ta-lib**

```
手动下载安装，而且需要下载对应Pyhon版本
https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
或者
https://github.com/cgohlke/talib-build/releases

例如：
cmd输入ipython显示Python版本为3.8.6
则pip install TA_Lib‑0.4.18‑cp38‑cp38‑win_amd64.whl
```

> **安装Mongodb数据库**（使用complete默认配置安装）

```
官方下载安装
https://www.mongodb.com/products/self-managed/community-edition
```

> **历史行情数据导入到Mongodb数据库**

```
1、确保历史行情数据文件(*.csv)放在 pond_backtesting/data 文件夹下
2、运行 pond_backtesting/utility.py 文件
```

> **开始回测**

```
1、确保模型信号文件(*.csv)放在 pond_backtesting/data 文件夹下
2、运行 pond_backtesting/run.py 文件开始回测
```

## Ubuntu系统


> **安装pip**

```
sudo apt update
sudo apt install python3-pip
```

> **安装依赖库**

```
pip3 install -r requirements.txt

如果报错"error: externally-managed-environment"，尝试以下命令
pip3 install -r requirements.txt --break-system-packages
```

> **安装ta-lib**

```
下载 TA-Lib 源码
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz

解压下载的文件
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/

编译和安装 TA-Lib
./configure --prefix=/usr
make
sudo make install

安装 Python 包
pip3 install ta-lib
```

> **安装Mongodb数据库**

```
官方教程
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu-tarball/
```

**历史行情数据导入到Mongodb数据库**

```
1、确保历史行情数据文件(*.csv)放在 pond_backtesting/data 文件夹下
2、运行 pond_backtesting/utility.py 文件
```

> **开始回测**

```
1、确保模型信号文件(*.csv)放在 pond_backtesting/data 文件夹下
2、运行 pond_backtesting/run.py 文件开始回测
```

## Ubuntu环境报错

使用pymongo报错：

pymongo.errors.AutoReconnect: localhost:27017: connection closed (configured timeouts: connectTimeoutMS: 20000.0ms)

pymongo.errors.OperationFailure: 24: Too many open files, full error: {'ok': 0.0, 'errmsg': '24: Too many open files', 'code': 264, 'codeName': 'TooManyFilesOpen'}

```
Mongodb被意外关闭，重新系统运行Mongodb。
mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork

pymongo.errors.OperationFailure: 24: Too many open files 错误表明你的系统已经达到或超过了文件描述符的限制。这可能是由于大量的 MongoDB 连接或其他进程消耗了大量文件描述符导致的。
ulimit -n 65536
```
