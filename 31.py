# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 08:48:26 2022

@author: KatayamaMasa
"""
def hoge(coins, target):
    # 大きい貨幣から順に使っていくイメージ
    cnt = 1 # 1pのみの場合は初めにカウントしておく
    for c in coins[:-1]: # forループは1pを除く
        # 使えるだけ使うパターンから順にやっていく
        for n in reversed(range(target//c)):
            amount = c * (n + 1)
            if amount == target:
                cnt += 1
            else:
                # 残りの貨幣と差額を渡して再帰呼び出し
                cnt += hoge(coins[coins.index(c)+1:], target-amount)
    return cnt



if __name__ == "__main__":
    coinList = [200,100,50,20,10,5,2,1]
    base = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coins.sort(reverse=True)
    print(hoge(coins, 200))            