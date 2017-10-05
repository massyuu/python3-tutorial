#!/usr/bin/env python

# 処理の実行時間を取得する
import time

startTime = time.time()

# 何か処理を行う
for i in range(100000):
    print(i)

passTime = time.time() - startTime
print ("実行時間:{0:.3f}".format(passTime) + "秒")
