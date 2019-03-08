# -*- coding: utf-8 -*-
import nmap
import sys, getopt
import openpyxl
import datetime
import time

# 函数 ReadExcel 用于将 nmap 数据写入 xlsx 文件
def WriteExcel(param,url,starttime):
    today = str(datetime.date.today())
    nowtime = time.strftime("%H-%M-%S")
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = url
    len1 = len(param)
    for i in range(0, len1):
        demo = param[i].split(';')
        len2 = len(demo)
        for j in range(0, len2):
            sheet.cell(row=i+1, column=j+1, value=str(demo[j]))
    wb.save('./'+url+'-'+today+'-'+nowtime+'.xlsx')
    print('#*# 文件：'+url+'-'+today+'-'+nowtime+'.xlsx 已经输出完毕')
    endtime = datetime.datetime.now()
    print ('耗时：'+str((endtime - starttime).seconds))



# 函数 NmapExcel 调用 python-nmap 使用 nmap 扫描
def NmapExcel(param1,param2):
    nm = nmap.PortScanner() #创建nmap接口
    website_urls = open('url.txt','r') #url.txt存储的是目标站点ip/url
    if website_urls:
        for url in website_urls:
            try:
                starttime = datetime.datetime.now()
                nm.scan(hosts=url, ports=param1, arguments=' -Pn -sV'+param2)
                # print(type(nm.csv()))   #host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe
                nmap_data = nm.csv().split('\n')
                WriteExcel(nmap_data,url,starttime)
            except Exception:
                print('扫描出错，当前扫描进行到：'+url)
    else:
        print("未读取到目标站点，请先添加目标")
    website_urls.close()



# 函数 StartFunc 用于输出相关参数的意义
def StartFunc(argv): 
    parameter1 = ''
    parameter2 = ''
    try:
        opts, args = getopt.getopt(argv,"hp:o:",["port=","other="])
    except getopt.GetoptError:
        print('python ./scan.py -p <需要扫描端口> -o <其他nmap参数>')
        print('使用 -h 查看详细用法')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python ./scan.py -p <需要扫描端口> -o <其他nmap参数>')
            print('目标 url 请放在当前目录下的 url.txt 文件内')
            print('-p  使用样例 -p port ，-p 1-65535')
            print('-o  默认使用 -Pn  -sV 参数，无需重复输入')
            print('注意：url只允许ip地址或者不带http/https头的域名地址')
            sys.exit()
        elif opt in ("-p", "--port"):
            parameter1 = arg
        elif opt in ("-o", "--other"):
            parameter2 = arg
    print('#*# NmapToExcel 正在运行')
    NmapExcel(parameter1,parameter2)
#    print(parameter1)
#    print(parameter2)




if __name__ == "__main__":
    print('''
         )\____________________________|¯¯¯¯¯|__,,,,,. 
      )_         ||||||||||||||||||||||||||||||||||||||||||||||||||||||||            |    | 
        /                    _________________         __|__| 
       /}}}}}}}}}}/(__\¯\¯                              |____| 
      /}}}}}}}}}}}/}}___\| 
     /}}}}}}}}}}}}}}/ 
    /}}}}}}}}}}}}}}/ 
   /}}}}}}}}}}}}}}/ 
  /}}}}}}}}}}}}}}/ 
 /}}}}}}}}}}}}}}/ 
/}}}}}}}}}}}}}}/ 
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

NmapToExcel version 1.0.0
time 2019-3-8
    ''')
    StartFunc(sys.argv[1:])