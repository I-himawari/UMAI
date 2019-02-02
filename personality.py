import numpy as np

def best_goods_per_personality(personality_list):
    # personality_list = [True, False, True, True, True, False, True, False, False]
    sl = np.loadtxt("shop.csv",delimiter=",")
    personality_table = np.zeros(3)
    personality_index = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    personality_index_is_valid = [True, True, True, True, True, False, True, True, False]
    result_list = ["マクドナルド","フレッシュネスバーガー","ラーメン二郎","ココイチ","陳麻家","さんるーむ","牛角","くら寿司","モスバーガー","木曽路","サブウェイ","味楽亭"]
    result_url = ["bigmac_l.png", "FRESHNESSBURGER_freshunessburger.jpg", "ramenjiro_ramen.jpg", "1777215.jpeg", "kv_02.jpg", "640x640_rect_46126601.jpg", "gyukaku_karubi.jpg", "kurazushi_salmon.jpg", "mosburger_mosburger.jpg", "P029661817_480.jpg", "subway_shrimpandavogado.jpg", "mirakutei-1.jpg"]

    for i, v, l in zip(personality_index, personality_index_is_valid, personality_list):
        personality_table[i] += v == l  # False（否定すると加算される問題）ならFalse（いいえ）を選択したら加点するようにする。

    personality_table /= 3  # 0~1に合わせる

    r = np.sum(np.square(sl - personality_table), axis=1)
    good_index = r.argmin()
    return [result_list[good_index], result_url[good_index]]