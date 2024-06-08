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
https://www.mongodb.com/products/self-managed/community-edition
```

> **行情数据文件导入到Mongodb数据库**

```
1、确保行情数据文件放在 pond_backtesting/data 文件夹下
2、运行 pond_backtesting/data/utility.py 文件
```

> **开始回测**

```
1、确保模型信号文件放在 pond_backtesting/data 文件夹下
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