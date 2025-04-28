import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['SQ', 'CQL', 'SNK', 'CQL|SNK', 'CQL&SNK'],
    'FL': [3, 78, 38, 94, 22],
    'FN': [0, 67, 20, 77, 10],
    'LN': [0, 65, 11, 70, 6]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 7))
bars1 = plt.bar(df['Category'], df['FL'], color='#99ff99', edgecolor='grey', label='FL')
bars2 = plt.bar(df['Category'], df['FN'], bottom=df['FL'], color='#3ea8ef', edgecolor='grey', label='FN')
bars3 = plt.bar(df['Category'], df['LN'], bottom=df['FL'] + df['FN'], color='#FF878B', edgecolor='grey', label='LN')

plt.xlabel('Tools', fontweight='bold', fontsize=16)
plt.ylabel('Total number of PNR', fontweight='bold', fontsize=16)
plt.xticks(rotation=0, ha="center", fontsize=14)

def add_value_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        if yval != 0:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + yval, int(yval), ha='center', va='bottom', fontsize=14)

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)

plt.legend(loc='upper right', fontsize=14)
plt.tight_layout()

plt.show()