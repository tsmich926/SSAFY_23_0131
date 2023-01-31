# s = input()
# l = set(s)
# print(l)
# lst = []
# for i in l:
#     print(i)
#     lst.append(i)
# li2 = list(s)
# li2.count()


# print(lst1)
# print(len(lst1))
# print(lst1[0])
# for i in range(len(lst1)): 
#     print(lst1[i])

# 문자열에 쓰인 단어수 출력
# s = input()
# l = set(s)
# print(l)
# lst = []
# li2 = list(s)
# for i in l:
#     # print(i)
#     cnt =li2.count(i)
#     print(i,cnt)
""""""""""""""""""""""""""""""""
#! 정답코드

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


#어짜피 대문자로 출력해야 하니 다 대문자로 바뀸
#set해서 중복 제거
#set한거 리스트1에 넣어서 하나씩 꺼내서 갯수세기
#빈리스트 리스트2에 센 갯수넣기 max로 누가 젤 큰지 보기
#max의 갯수가 두개이상이면 ?출력
#아니면 인덱스 출력한 뒤 리스트1[인덱스]해서 어떤 알파벳이 가장 많은지 확인
#이미 다 대문자로 바꿔서 대문자로 출력될거임.

# if 문자열.isupper() == False: 대문자가 아니면~
    # 문자열.upper() #해당 문자열을 대문자로 변환

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
    if alpa.isupper() == False:
        print(alpa.upper())
    else:
        print(alpa)