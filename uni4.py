var6 = ['разработка', 'администрирование', 'protocol', 'standard']
for i in var6:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))
    print('#'*15)