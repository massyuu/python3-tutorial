#!/usr/bin/env python

'''
【内包表記】
'''

# リスト内包表記
# [Counter for Counter in Iterator]

# 単純なリスト
print("---------simple---------")
list = [num for num in range(0, 10)]
print(list)

# if条件追加
print("---------if---------")
list = [num for num in range(0, 10) if num % 2 == 1]
print(list)

# if-else条件追加(三項演算子)
print("---------if-else---------")
list = [num if num % 2 == 1 else num * 10 for num in range(0, 10)]
print(list)

# ネスト
# 網羅的な組み合わせ
print("---------nest---------")
listA = range(1, 5)
listB = range(1, 4)
mixList = [[listAItem, listBItem] for listAItem in listA for listBItem in listB]
for mixListItem in mixList:
    print(mixListItem)

# 辞書内包表記
print("---------dict---------")
list = [[1, "a"], [2, "b"], [3, "c"]]
dict = {key: value for key, value in list}
print(dict)

# セット内包表記
print("---------set---------")
set = {num for num in range(1,10) if num%2 == 1}
print(set)

# タプルには内包表記
# 正確にはリストをタプル化
print("---------list to tuple---------")
tuple = tuple([num for num in range(0, 10)])
print(tuple)

# ジェネレータ内包表記
print("---------generator---------")
numTuple = (num for num in range(1,10))
for num in numTuple:
    print(num)
