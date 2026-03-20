##########################################
####author:Anzilz1972
####date: 2026-3-16
####Python编程：Fluent Python 练习 
####第二章：探索元组和列表-->拆包
##########################################

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"西半球城市":>10} | {"latitude":>9} | {"longitude":>9}')
    ####嵌套拆包
    for name, _, _, (lat, lon) in metro_areas: 
        if lon <= 0: 
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
    

    print("\n====================\n")

    ####使用序列模式匹配 match/case语法
    print(f'{"东半球城市":>10} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            #列表、元组或多个变量都可以匹配任何序列，如下：
            #case [str(name), *_, (float(lat), float(lon)) as coord] if lon >= 0:
            #case str(name), *_, (float(lat), float(lon)) as coord if lon >= 0:
            case (str(name), *_, (float(lat), float(lon)) as coord) if lon >= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f} | {coord}')

if __name__ == '__main__':
    main()