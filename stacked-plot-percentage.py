import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['SQ', 'CQL', 'SNK', 'CQL|SNK', 'CQL&SNK'],
    'FL': [100, 66.67, 92.11, 71.28, 90.91],
    'FN': [0, 34.33, 70, 41.56, 40],
    'LN': [0, 21.54, 54.55, 25.71, 33.33]
}

df = pd.DataFrame(data)

plt.figure(figsize=(6, 5))
bars1 = plt.bar(df['Category'], df['FL'], color='#99ff99', edgecolor='grey', label='FL')
bars2 = plt.bar(df['Category'], df['FN'], bottom=df['FL'], color='#3ea8ef', edgecolor='grey', label='FN')
bars3 = plt.bar(df['Category'], df['LN'], bottom=df['FL'] + df['FN'], color='#FF878B', edgecolor='grey', label='LN')

plt.xlabel('Tools', fontsize=16)
plt.ylabel('Percentage of unrecognized patches', fontsize=16)
plt.xticks(rotation=0, ha="center", fontsize=14)

def add_value_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        if yval != 0:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + yval, f'{yval:.2f}%', ha='center', va='bottom', fontsize=14)

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)

plt.legend(loc='upper right', fontsize=14)
plt.tight_layout()

plt.show()