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

> **安装依赖库**

```
python3 -m pip3 install -r requirements.txt --break-system-packages
```

> **安装ta-lib**

```
TA-Lib 需要一些编译工具和依赖库。可以通过以下命令安装这些依赖
sudo apt update
sudo apt install build-essential
sudo apt install python3-dev
sudo apt install libta-lib0 libta-lib0-dev

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