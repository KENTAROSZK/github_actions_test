import numpy as np

# ランダムな整数を2つ持つ配列を生成
random_integers = np.random.randint(1, 100, size=2)

# 配列を.txtファイルに出力
with open('./src/output.txt', 'w') as f:
    f.write(','.join(map(str, random_integers)))
