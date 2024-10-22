# output.txtファイルを読み取る
with open('output.txt', 'r') as f:
    data = f.read()

# 整数をリストに変換
numbers = list(map(int, data.split(',')))

# 合計を計算
total = sum(numbers)

# 合計を表示
print(f'The sum of the integers is: {total}')
