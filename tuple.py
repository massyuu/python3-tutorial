#!/usr/bin/env python

'''
【タプル】
'''
from operator import itemgetter, attrgetter
import copy

tuple = ("banana", "apple", "cherry")
multiLTuple = (("banana",1) ,("apple",3) ,("cherry",2))

# 要素の取得
# tuple[開始インデックス:終了インデックス]
print("---------item---------")
print(tuple[1:2])
print(tuple[1:])
print(tuple[:2])

# 要素の存在確認
# XXXX in tuple
print("---------in tuple---------")
print("apple" in tuple)
print("orange" in tuple)

# インデックスの取得
# tuple.index(XXX)
print("---------index---------")
print(tuple.index("banana"))

# 指定のオブジェクトの要素の個数
# tuple.count(XXX)
print("---------count---------")
print(tuple.count("banana"))

# ソート（元のタプルを保持する）
# ※他のイテラブルも可
print("---------sorted---------")
result = sorted(tuple)
print(result)

# operatorモジュール関数(itemgetter(), attrgetter(), methodcaller())
# sorted(tuple, key=itemgetter(index), reverse=True)
print("---------sorted itemgetter---------")
print(sorted(multiLTuple, key=itemgetter(1), reverse=True))

# タプルの連結
# newTuple = tupleA + tupleB
print("---------tuple combine---------")
tupleA = (1, 6, 9)
tupleB = (3, 7, 5)
newTuple = tupleA + tupleB
print(newTuple)

# タプルの連結（複数回）
# newTuple = tuple * 回数
print("---------tuple * count---------")
newTuple = tupleA * 3
print(newTuple)

# 複数タプルからタプルのイテレータを生成
# python3ではzipはイテレータを返す
print("---------zip---------")
tupleA = (1, 6, 9)
tupleB = (3, 7, 5)
tupleTupleIterator = zip(tupleA, tupleB)
for tupleItem in tupleTupleIterator:
    print(tupleItem)
