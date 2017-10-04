#!/usr/bin/env python

'''
【リスト】
'''
from operator import itemgetter, attrgetter
import copy

list = ["banana", "apple", "cherry"]
multiLList = [["banana",1], ["apple",3], ["cherry",2]]

# 要素の取得
# list[開始インデックス:終了インデックス]
print("---------item---------")
print(list[1:2])
print(list[1:])
print(list[:2])

# 要素の存在確認
# XXXX in list
print("---------in list---------")
print("apple" in list)
print("orange" in list)

# インデックスの取得
# list.index(XXX)
print("---------index---------")
print(list.index("banana"))

# 指定のオブジェクトの要素の個数
# list.count(XXX)
print("---------count---------")
print(list.count("banana"))

# ソート（元のリストを保持する）
# ※他のイテラブルも可
print("---------sorted---------")
result = sorted(list)
print(result)

# operatorモジュール関数(itemgetter(), attrgetter(), methodcaller())
# sorted(list, key=itemgetter(index), reverse=True)
print("---------sorted itemgetter---------")
print(sorted(multiLList, key=itemgetter(1), reverse=True))

# ソート（元のリストを保持しない）
# list.sort()
print("---------sort---------")
list2 = list.copy()
list2.sort()
print(list2)
print(list)

# リストの追加（要素）
# list.append(XXX)
print("---------append---------")
list.append("pen")
print(list)

# リストの追加（リスト）
# listA.extend(listB)
print("---------extend---------")
listB = [3, 7, 5]
list.extend(listB)
print(list)

# リストの連結
# newList = listA + listB
print("---------list combine---------")
listA = [1, 6, 9]
listB = [3, 7, 5]
newList = listA + listB
print(newList)

# リストの連結（複数回）
# newList = list * 回数
print("---------list * count---------")
newList = listA * 3
print(newList)

# リストへの挿入
# list.insert(index, XXX)
print("---------insert---------")
listA = [1, 6, 9]
listA.insert(2, 8)
print(listA)

# 複数リストからタプルのイテレータを生成
# python3ではzipはイテレータを返す
print("---------zip---------")
listA = [1, 6, 9]
listB = [3, 7, 5]
tupleListIterator = zip(listA, listB)
for tupleItem in tupleListIterator:
    print(tupleItem)

# 浅いコピー
# copy.copy(list)
print("---------copy---------")
listA = [1, 2, 3]
listB = listA
listC = copy.copy(listA)
listA[1] = 5
print(listA)
print(listB)
print(listC)

# 深いコピー
# copy.deepcopy(list)
print("---------deepcopy---------")
multiListA = [{1:"A", 2:"B"}, {3:"C", 4:"D"}, {5:"E", 6:"F"}]
multiListB = multiListA
multiListC = copy.copy(multiListA)
multiListD = copy.deepcopy(multiListA)
multiListA[0] = [0, 9]
multiListA[1][3] = "ZZZ"
print(multiListA)
print(multiListB)
print(multiListC)
print(multiListD)
