# 집합

# 집합의 표현
s1 = set([1, 2, 3])
s1 # {1, 2, 3}
s2 = set('Hello')
s2 # { 'e', 'l', 'o', 'H' }

# 집합의 값을 인덱싱으로 접근
s1 = set([1, 2, 3])
l1 = list(s1) # [1, 2, 3]
l1[0] # 1
l1 = tuple(s1)
l1 # (1, 2, 3)
l1[0] # 1

# 집합 자료형의 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
s1 & s2 # { 4, 5, 6 }
s1.intersection(s2) # { 4, 5, 6 }

# 합집합
s1 | s2 # { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
s1.union(s2) # { 1, 2, 3, 4, 5, 6, 7, 8, 9 }

# 차집합
s1 - s2 # { 1, 2, 3 }
s2 - s1 # { 8, 9, 7 }
s1.difference(s2) # { 1, 2, 3 }
s2.difference(s1) # { 8, 9, 7 }

# 값 1개 추가하기
s1 = set([1, 2, 3])
s1.add(4)
s1 # { 1, 2, 3, 4 }

# 값 여러 개 추가하기
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1 # { 1, 2, 3, 4, 5, 6 }

# 특정 값 제거하기
s1 = set([1, 2, 3])
s1.remove(2)
s1 # { 1, 3 }
