# 回测系统使用指南（系统环境建议 Windows Server 2019 Datacenter）

> **安装Anaconda**推荐

```
https://repo.continuum.io/archive/.winzip/ 
安装时注意将后面的添加为系统环境变量选项打勾

【推荐版本】
Anaconda3-2021.11-Windows-x86_64.zip	507.5M	2021-11-17 12:10:52 (Python 3.9.7)
```

> **安装VNPY**

```
点击【vnpy\install.bat】文件，包含安装需要的第三方Pyhon库和其他准备内容
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