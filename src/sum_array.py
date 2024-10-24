import os

# 環境変数から出力ファイル名を取得
file_name = os.getenv('INPUT_FILE', 'output.txt')

# output.txtファイルを読み取る
with open(file_name, 'r') as f:
    data = f.read()

# 整数をリストに変換
numbers = list(map(int, data.split(',')))

# 合計を計算
total = sum(numbers)

# 合計を表示
print(f'The sum of the integers is: {total}')
