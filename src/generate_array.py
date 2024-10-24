import numpy as np
import os

# 環境変数から出力ファイル名を取得
file_name = os.getenv('OUTPUT_FILE', 'src/output.txt')

# ランダムな整数を2つ持つ配列を生成
random_integers = np.random.randint(1, 100, size=2)

# 配列を.txtファイルに出力
with open(file_name, 'w') as f:
    f.write(','.join(map(str, random_integers)))
