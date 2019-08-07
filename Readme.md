## NmapToExcel

使用 python 调用 nmap 进行批量扫描，并将结果写入本地xlsx文件

## 环境需求

```
//linux 系统
sudo apt-get nmap
sudo pip install python-nmap

//windows 系统
若 python 有安装 nmap 库，必须卸载

//只支持 python3 版本
sudo pip install python-nmap
sudo pip install openpyxl
or
sudo pip install -r requirements.txt

遇到nmap相关报错问题，建议卸载重装python-nmap
```

## 参数配置
```
usage: python ./scan.py -p <需要扫描端口> -o <其他nmap参数>

目标 url 请放在当前目录下的 url.txt 文件内

-p  使用样例 -p port ，-p 1-65535
-o  默认使用 -Pn  -sS -sU 参数，无需重复输入

注意：url只允许ip地址或者不带http/https头的域名地址     
```

------------------------------------------
v1.1更新

- 增加多线程处理
- 增加对结果xlsx表格的宽度自适应处理

演示效果图：
![](images/2019-08-07-10-38-55.png)