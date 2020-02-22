# 1108.IP地址无效化
#
# 给你一个有效的IPv4地址address，返回这个IP地址的无效化版本。
# 所谓无效化IP地址，其实就是用"[.]"代替了每个"."。
#
# 示例1：
# 输入：address = "1.1.1.1"
# 输出："1[.]1[.]1[.]1"
#
# 示例2：
# 输入：address = "255.100.50.0"
# 输出："255[.]100[.]50[.]0"
#
# 提示：给出的address是一个有效的IPv4地址


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
