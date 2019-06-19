# 70.爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。




#动态规划找出规律
#然后依据规律进行递归求解
def climbStairs( n: int) -> int:
    #起始值n=1的情况
    if n == 1:
        ans = 1
        return ans
    # 起始值n=2的情况
    if n == 2:
        ans = 2
        return ans
    #找出的规律，递归求解
    ans=climbStairs(n-1)+climbStairs(n-2)
    return ans

print(climbStairs(7))