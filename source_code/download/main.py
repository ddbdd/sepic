import requests
import time
from os import environ as en
from os import mkdir as mk
en['REQUESTS_CA_BUNDLE'] =  'cacert.pem'
try:
    mk('download')
except:
    print("download文件夹已存在")
result = []
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
tmph = {'User-Agent':'downloaderv1'}
ok = 0
w = 0
fail = []
fail_se = []
print("正在向zzx的服务器请求准许运行状态码，请保证网络连接正常")
time.sleep(1)
while (ok !=1 and w <15):
    try:
        r = requests.get('https://test.xzzzx.xyz/1.html',headers = tmph)
        if r.status_code == 200:
            ok = 1
            r.encoding = 'utf8'
            b = r.text
    except:
        w += 1
        print("请求状态码失败，正在重试......")
if ok != 1:
    print("网络异常或zzx不允许您使用本软件")
    input('按任意键退出')
    quit()
else:
    print("准许运行！以下是来自zzx的服务器的最新公告：")
    print('*'*55)
    print(b)
    print('*'*55)
print()
print("您想下载横屏(电脑)图片还是竖屏(手机)图片？")
print("下载竖屏图片请输入1，下载横屏请输入2")
print()
tt = input("请输入1或2:  ")
while tt not in ('1','2'):
    tt = input("请输入1或2")
if tt == '1':
    urls = 'out_sj.txt'
elif tt == '2':
    urls = 'out_dn.txt'
with open(urls,'r',encoding='utf8') as file:
    m = file.readlines()
    for x in m:
        p = x.rstrip('\n')
        result.append(p)
total = len(result)
print(f"总共有{total}张照片可供下载")
start = input("您希望从第几张开始下载？")
while not (str.isdigit(start) and 0<int(start)<total):
    start = input("您希望从第几张开始下载？")
end = input("您希望下载到第几张结束？")
while not (str.isdigit(end) and int(start)<int(end)<=total):
    end = input("您希望从第几张开始下载？")
start = int(start)
end = int(end)
print("遵命！即将开始下载")
time.sleep(3)
for i in range(start,end+1):
    src = result[i-1]
    geshi = src[-4:len(src)]
    try:
        print(f'正在下载第{i}张')
        file_name = 'download/' + str(i) + geshi
        pic = requests.get(src,headers=header)
        with open(file_name, 'wb') as file:
            file.write(pic.content)
    except:
        print(f'*******************************第{i}张下载失败')
        fail.append(src)
        fail_se.append(i)
while len(fail_se) != 0:
    print("共失败",len(fail_se),"项")
    print("##################正在重新下载失败项")
    time.sleep(1.5)
    x = 0
    for i in fail_se:
        src = fail[x]
        geshi = src[-4:len(src)]
        try:
            print(f'正在下载第{i}张')
            file_name = 'download/' + str(i) + geshi
            pic = requests.get(src,headers=header)
            with open(file_name, 'wb') as file:
                file.write(pic.content)
            fail.pop(x)
            fail_se.pop(x)
        except:
            print(f'*******************************第{i}张下载失败')
print("下载完成")
input("按任意键退出")