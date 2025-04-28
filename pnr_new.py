import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['SQ', 'CQL', 'SNK', 'CQL|SNK', 'CQL&SNK'],
    'FL': [3, 78, 38, 94, 22],
    'FN': [0, 67, 20, 77, 10],
    'LN': [0, 65, 11, 70, 6]
}

pnr_data = {
    'FL': [3, 52, 35, 67, 20],
    'FN': [0, 23, 14, 32, 4],
    'LN': [0, 14, 6, 18, 2]
}

df = pd.DataFrame(data)

ax = df.plot(kind='bar', x='Category', stacked=False, figsize=(10, 6), color=['#99ff99', '#3ea8ef', '#FF878B'], edgecolor='grey')

for i, category in enumerate(data['Category']):
    bar1 = ax.bar(i - 0.2, pnr_data['FL'][i], width=0.1, color='#9370DB', label='PNR' if i == 0 else "")
    bar2 = ax.bar(i, pnr_data['FN'][i], width=0.1, color='#9370DB')
    bar3 = ax.bar(i + 0.2, pnr_data['LN'][i], width=0.1, color='#9370DB')

    if pnr_data['FL'][i] > 0:
        ax.text(i - 0.2, pnr_data['FL'][i] + 2, f'{pnr_data["FL"][i]}', ha='center', va='bottom', fontsize=10, color='red')
    if pnr_data['FN'][i] > 0:
        ax.text(i, pnr_data['FN'][i] + 2, f'{pnr_data["FN"][i]}', ha='center', va='bottom', fontsize=10, color='red')
    if pnr_data['LN'][i] > 0:
        ax.text(i + 0.2, pnr_data['LN'][i] + 2, f'{pnr_data["LN"][i]}', ha='center', va='bottom', fontsize=10, color='red')

for bars in ax.containers:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{int(height)}', ha='center', va='bottom', fontsize=10, color='black')

plt.xlabel('Tools', fontsize=16)
plt.ylabel('TPs with PNR Annotations', fontsize=16)
plt.xticks(rotation=0, fontsize=14)
plt.yticks(fontsize=14)

plt.legend(['TPs at FL', 'TPs at FN', 'TPs at LN', 'PNR'], fontsize=14)

plt.tight_layout()
plt.show()