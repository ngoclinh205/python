_list = ['abc', 'hello', 'hi', 'python', 'ok']

n = int(input("Nhập n: "))

result = []

for i in _list:
    if len(i) > n:
        result.append(i)

print(result)