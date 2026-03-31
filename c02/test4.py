##########################################
####author:Anzilz1972
####date: 2026-3-16
####Python编程：Fluent Python 练习 
####第二章：探索元组和列表-->数组
##########################################

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])

if(floats == floats2):
    print('\ntwo array Equal')
else:
    print('\ntow array is not Equal!')


step = 1000
for start in range(step):
    print(f'=======第 {start + 1} 个切片=======\n')
    sf1 = floats[start::step]
    for idx in range(10): #每个切片只打印前十个数字
        print(sf1[idx])






