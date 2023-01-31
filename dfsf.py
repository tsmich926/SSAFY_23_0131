# s = input()
# for i in s:
#     print(i)
#     if isupper(i) ==

s = input()
s = s.upper()
l = set(s)
li2 = list(l)
# print(li2)
lst2 = []
for i in li2:
    cnt = s.count(i)
    # print(cnt)
    lst2.append(cnt)
# print(lst2)
if lst2.count(max(lst2)) > 1:
    print('?')
else:
    max_idx = lst2.index(max(lst2))
    alpa = li2[max_idx]
    print(alpa)