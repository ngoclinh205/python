#loại bỏ tất cả phần tử trùng
_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

_new = []

for i in _list:
    if _list.count(i) == 1:
        _new.append(i)

print(_new)

#loại bỏ trùng nhưng giữ 1 ptu
_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

_new = []

for i in _list:
    if i not in _new:
        _new.append(i)

print(_new)