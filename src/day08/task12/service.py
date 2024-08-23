# day08 > task12 > service.py
f = open("아파트(매매)_실거래가_20240823.csv", 'r')
data = []

while True:
    line = f.readline().strip().replace("\"","").split(",")
    print(line)
    if line[0] == "NO":
        break
while True:
    line = f.readline().strip().replace("\"","").split(",")
    if line == ['']:
        break
    print(line)


def getall():



    return