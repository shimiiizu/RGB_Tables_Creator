import pandas as pd

# 刻み幅 5 の場合
step = 1
rgb_values = list(range(0, 256, step))

rgb_combinations = []
for r in rgb_values:
    for g in rgb_values:
        for b in rgb_values:
            rgb_combinations.append([r, g, b])

df = pd.DataFrame(rgb_combinations, columns=['R', 'G', 'B'])
df.to_csv('./csv/RGB_step5.csv', index=False)

print(f"Step={step}: {len(df)}個の組み合わせ")
# 出力: Step=5: 132651個の組み合わせ (51 x 51 x 51)