##########################################
####author:Anzilz1972
####date: 2026-3-16
####Python编程：Fluent Python 练习 
####第二章：探索元组和列表
##########################################
import dis


#####观察列表和元组的字节码实现
def fun1():
    numlist = [1,2,3,4,5]
    numtuple = (1,2,3,4,5)
    return

print("\n=======")
dis.dis(fun1)
print("\n=======")
dis.show_code(fun1)


#####检测元组的值是否固定
def fixed(obj):
    try:
        hash(obj)
    except TypeError:
        return False
    return True

a = (1,2,3,4,5)
print(fixed(a))

b = (23,'what are you doing?',[22,33,44])
print(fixed(b))









