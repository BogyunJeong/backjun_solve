from collections import deque
from typing import List

class Contry:
    def __init__(self,mFreq,mY,mX):
        self.mFreq = mFreq
        self.mY = mY
        self.mX = mX

id2idx = {}
bucket_size = 100
bucket_num = (_N // bucket_size) + 1
bucket = [[[] for _ in range(bucket_num)] for _ in range(bucket_num)]

def init(N : int, mLimit : int) -> None:
    global _N,_mLimit,bucket
    _N = N
    _mLimit = mLimit
    id2idx.clear()


def addRadio(K : int, mID : List[int], mFreq : List[int], mY : List[int], mX : List[int]) -> None:
    for i in range(K):
        contry = Contry(mFreq[i],mY[i],mX[i])
        id2idx[mID[i]] = contry
        bucket[mY[i]// bucket_size][mX[i]//bucket_size].append(contry)

def getMinPower(mID : int, mCount : int) -> int:
    r,c,f = id2idx[mID]
    b_r,b_c = r // bucket_size, c // bucket_size
    power_cnt = [0 for _ in range(2 * _N + 101)]
    C = mCount
    bucket_cnt = [0 for _ in range(31)]

    weight = 1

    dr = [1,-1,0,0]
    dc = [0,0,-1,1]
    for row,col,freq in bucket[b_r][b_c]:  
        if r  == row and c == col and f == freq: continue

        power = abs(r - row) + abs(c - col) + 100*(f != freq)
        if power <= _mLimit:
            bucket_cnt[(power - 1) // 100] += 1
            power_cnt[power] += 1

    while True:
        b_r -= 1
        b_col -= 1

        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            for _ in range(weight*2):
                b_r += dx
                b_col += dy
                if 0 <= b_r < bucket_num and 0 <= b_r < bucket_num:
                    for row,col,freq in bucket[b_r][b_c]:
                        power = abs(r - row) + abs(c - col) + 100 *(f != freq)
                        if power <= _mLimit:
                            bucket_cnt[(power-1)//100] += 1
                            power_cnt[power] += 1

        if bucket_cnt[weight-1] > C:
            break
        bucket_cnt[weight] += bucket_cnt[weight-1]
        weight += 1

    idx, ans, cnt = 1,0,0
    while cnt < C:
        if power_cnt[idx]:
            temp = min(power_cnt[idx], C - cnt)
            cnt += temp
            ans += temp * idx
        idx += 1

    return ans * 10