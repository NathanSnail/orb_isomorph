with open("D:/Steam/steamapps/common/Noita/noita.exe", "rb") as f:
    txt = f.read()


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


match = input("pattern: ")
for off in range(1, 100):
    print(off)
    for alpha in range(off):
        sl = txt[alpha::off]
        for i in range(2**8):
            m = [x for x in find_all(
                sl, bytes([bytes(x, encoding="utf-8")[0] ^ i for x in match]))]
            if len(m):
                print(m, i)
