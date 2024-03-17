put = int(input('請輸入:'))
for z in range(put):
    print(" " * (put - 1 - z) + "*" * (z * 2 + 1))
for z in range(put):
    print(" " * (put - 1) + "*")
