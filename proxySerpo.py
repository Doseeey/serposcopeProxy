import urllib.request

url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt'
source_code = urllib.request.urlopen(url).read().decode()
split_source = source_code.split('\n')

ips = []
for s in split_source[8:-1]:
    x = s.split()
    if len(x) == 3:
        ips.append(x[0])

print(split_source[0])
for ip in ips:
    rdy = ip.split(":")
    print('http#'+rdy[0]+'#'+rdy[1])

input()