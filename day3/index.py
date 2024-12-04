import re

sample_text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# regex = "/mul\([\d,]*\)/g"

f = open("input")
problem_set = f.read()

output = re.findall("(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))", problem_set)
# this regex is returning tuple with each group
# can use to modify the function, detect which index is != ""
# act accordingly

# print(f"The output of regex \n {output}")

def flagOrMulToInt(a_output):
    flag = True
    total = 0
    for t_output in a_output:
        if t_output[0]:
            if flag:
                total += mulToInt(t_output[0])
        elif t_output[1]:
            flag = True
        elif t_output[2]:
            flag = False
        else:
            print("You really shouldn't be seeing this.")
    return total



def mulToInt(mul_statement):
    print(f"mul_statement 1: {mul_statement}")
    split_mul = mul_statement.split("(")
    strip_mul = split_mul[1].strip(")")
    s_nums = strip_mul.split(",")
    print(f"s_nums: {s_nums}")
    print(f"s_nums are {s_nums[0]}, {s_nums[1]}")
    total = int(s_nums[0]) * int(s_nums[1])
    print(f"{mul_statement} is {s_nums[0]} * {s_nums[1]} = {total}")
    return total

mulTotal = flagOrMulToInt(output)
print(f"\n The findings arreeee :: {mulTotal}")
"""
total = 0
for mul in output:
    total += mulToInt(mul)
"""
# print(f"The absolute total is: {total}")
