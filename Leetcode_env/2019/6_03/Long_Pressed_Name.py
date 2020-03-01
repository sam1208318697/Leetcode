# 925. 长按键入

# 你的朋友正在使用键盘输入他的名字name。偶尔，在键入字符c时，按键可能会被长按，而字符可能被输入1次或多次。
# 你将会检查键盘输入的字符typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回True。

# 示例1：
# 输入：name = "alex", typed = "aaleex"
# 输出：true
# 解释：'alex'中的'a'和'e'被长按。

# 示例2：
# 输入：name = "saeed", typed = "ssaaedd"
# 输出：false
# 解释：'e'一定需要被键入两次，但在typed的输出中不是这样。

# 示例3：
# 输入：name = "leelee", typed = "lleeelee"
# 输出：true

# 示例4：
# 输入：name = "laiden", typed = "laiden"
# 输出：true
# 解释：长按名字中的字符并不是必要的。


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        name_list = []
        for i in name:
            name_list.append(i)
        typed_list =[]
        for i in typed:
            typed_list.append(i)


        if len(typed_list)>len(name_list):

            pos_name_list = 0
            pos_typed_list = 0
            while pos_typed_list<len(typed_list):
                if name_list[pos_name_list] == typed_list[pos_typed_list]:
                    if pos_name_list==len(name_list)-1:
                        pos_name_list = len(name_list)-1
                    else:
                        pos_name_list += 1

                    pos_typed_list += 1
                else:
                    if typed_list[pos_typed_list]==name_list[pos_name_list-1]:
                        pos_typed_list += 1
                    else:
                        return False
            if typed_list[-1]==name_list[-1]:

                return True
            else:
                return False

        elif len(typed_list) == len(name_list):

            if typed_list==name_list:
                return True
            else:
                return False

        else:
            return False


sol = Solution()
#print(sol.isLongPressedName("vtkgn","vttkgnn"))
print(sol.isLongPressedName("lrz","llrr"))