import requests
import time
result2 = list()
header = {'User-Agent':''}
try:
    with open('out_dn.txt','r',encoding='utf8') as file:
        m = file.readlines()
        for x in m:
            p = x.rstrip('\n')
            result2.append(p)
except:
    pass
#a = requests.get("http://hsapi.ipq.co/sj/",headers=header,allow_redirects=False)
def get_loc():
    a = requests.get("http://echs.sgslpx.com/dn/",headers=header,allow_redirects=False)
    b = a.headers['Location']
    return b
def one():
    global result2
    result = set()
    print(str(o) + '#'*10)
    oo = 0
    for i in range(20):
        try:
            m = get_loc()
            result.add(m)
            #time.sleep(0.5)
            print(i)
        except:
            if oo % 2 == 0:
                a = requests.get("http://hsapi.ipq.co/dn/",headers=header,allow_redirects=False)
            i = i - 1
            oo == oo + 1
            print('Failed,Retrying',oo)
    with open('out_dn.txt','a',encoding='utf8') as output:
        try:
            for x in result:
                if x not in result2:
                    result2.append(x)
                    output.writelines(x+'\n')
        except:
            pass
for o in range(50000):
    one()
print(len(result2))