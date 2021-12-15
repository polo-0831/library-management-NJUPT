def cal(string):
    S = sum([i * int(j) for i, j in zip(range(10, 1, -1), "".join(string.split('-')))])

    N = 11 - S % 11
    if N == 10: return string + '-X'
    if N == 11: return string + '-0'
    return string + '-' + str(N)


# ISBN号格式为X-XXX-XXXXX-X，输入X-XXX-XXXXX即可生成完整的ISBN号，如以下例子
print(cal('1-111-11111'), cal('2-222-22222'), cal('3-333-33333'))
