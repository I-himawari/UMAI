import numpy as np

def best_goods_per_personality(personality_list):
    # personality_list = [True, False, True, True, True, False, True, False, False]
    sl = np.loadtxt("shop.csv",delimiter=",")
    personality_table = np.zeros(3)
    personality_index = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    personality_index_is_valid = [True, True, True, True, True, False, True, True, False]
    result_list = ["マクドナルド","フレッシュネスバーガー","ラーメン二郎","ココイチ","陳麻家","さんるーむ","牛角","くら寿司","モスバーガー","木曽路","サブウェイ","味楽亭"]

    for i, v, l in zip(personality_index, personality_index_is_valid, personality_list):
        personality_table[i] += v == l  # False（否定すると加算される問題）ならFalse（いいえ）を選択したら加点するようにする。

    personality_table /= 3  # 0~1に合わせる

    r = np.sum(np.square(sl - personality_table), axis=1)
    return result_list[r.argmin()]