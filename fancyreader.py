import json
from pprint import pprint

with open('.\\files\\convo1.json') as data_file:
    data = json.load(data_file)
# pprint(data)

totalblocks=data['Blocks']
Block="Block"

# for i in range (totalblocks):
#     Cb=Block+str(i+1)
#
#     Cc=data[Cb]['convo']+".txt"
#     # print(Cc,Cb)
#
#     with open (Cc) as f:
#         content=f.read().splitlines()
#     for line in content:
#         print (line)

Cb=Block+"1"

Cc=data[Cb]['convo']+".txt"
# print(Cc,Cb)

with open (Cc) as f:
    content=f.read().splitlines()
for line in content:
    print (line)
for i in range(data[Cb]['answers']):
    print(i+1,".",data[Cb]['responses'][i]['text'])
