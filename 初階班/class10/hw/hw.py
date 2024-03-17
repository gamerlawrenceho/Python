# 1. 新增科目與成績
# 2. 刪除某個科目的成績
# 3. 關閉系統
# 每回合都要顯示目前的成績以及功能清單

d = {}
while True:
    for key, value in d.items():
        print(f'{key} = {value}')
    print("1. 新增科目與成績")
    print("2. 刪除某個科目的成績")
    print("3. 關閉系統")
    ans = input("請輸入功能編號:")
    if ans == "3":
        break
    elif ans == "2":
        l = input("刪除某個科目的成績:")
        d.pop(l, '')
    elif ans == "1":
        key = input("新增科目:")
        value = input("新增成績:")
        d[key] = value
    else:
        print("error")