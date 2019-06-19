# 69.x的平方根
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。



#---------------------遍历法---------------------

# def mySqrt(x: int) -> int:
#     i = 0
#     while True:
#         if x == i*i:
#             return i
#         elif x > i*i:
#             i = i + 1
#         else:
#             return i-1
#
# print(mySqrt(2115854281))



#---------------------二分法---------------------
# def mySqrt1(x: int) -> int:
#     i = int(x / 2)
#     while True:
#         if x == i*i or (i*i<x and (i+1)*(i+1)>x):
#             return i
#         elif x < i * i:
#             i=int(i/2)
#         else:
#             i=i+1
#
#
# print(mySqrt1(1307834445))


#---------------------牛顿迭代法---------------------

def mySqrt2(x: int) -> int:
    if x <= 1:
        return x
    r = x
    while r > x / r:
        r = (r + x / r) // 2
    return int(r)

print(mySqrt2(100))