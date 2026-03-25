# Definition for singly-linked list.
import array
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = array.array('i', [])
        arr2 = array.array('i', [])
        arres = array.array('i',[])
        
        nodetmp = ListNode()
        #将l1中各节点的val值保存在arr1中
        nodetmp.val, nodetemp.next =l1[0].val, l1[0].next
        while True:
            arr1.append(nodetmp.val)
            if nodetmp.next != None:
                nodetmp = nodetmp.next
            else:
                break

        #将l2中各节点的val值保存在arr2中
        nodetmp.val, nodetemp.next =l2[0].val, l2[0].next
        while True:
            arr2.append(nodetmp.val)
            if nodetmp.next != None:
                nodetmp = nodetmp.next
            else:
                break
        
        #始终保证arr1的成员数量>= arr2的成员数量
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        #将arr1 和arr2 的成员按对应位置一一相加
        #如果结果大于10，则用函数divmod计算出模（只能为1）余(mod)
        #将mod存储为arr3的对应位置成员，模作为进位数进入下一组数的运算
        carryvalue = 0
        for item in arr1:
            add_result = carryvalue    #当前位的和，等于前一位和的进位数
            idx = arr1.index(item)
            if idx < len(arr2):
                add_result = item + arr2[idx]
            else: #arr2已经到了最后一个成员
                add_result += item
            
            #处理当前两个数相加的和，形成当前位和进位数
            carryvalue, add_result = divmod(add_result, 10)
            arres.append(add_result)
        
        result_node = []
        p = ListNode()
        idx = 0
        while True:
            p.val = arres[idx]
            if idx < len(arres) -1:  #处理列表的最后一位之前的元素 
                p.next = ListNode()  #后面还有成员，可以生成新节点
                result_node.append(p)
                p = p.next
            elif idx == len(arres) -1: #处理到列表的最后一位了 
                p.next = None         #后续没有需要处理的成员，下一节点为空
                result_node.append(p)
                break
            else:
                pass
            idx += 1
        return result_node