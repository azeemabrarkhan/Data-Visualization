import matplotlib.pyplot as plt

tools = ['SQ', 'CQL', 'SNK']
precision = [1,1,1]
recall = [0.015228426395939087, 0.39593908629441626, 0.19289340101522842]
f1_score = [0.030000000000000002, 0.5672727272727273, 0.32340425531914896]

fig, ax = plt.subplots(figsize=(6, 5))

bar_width = 0.25

r1 = range(len(tools))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

bars1 = ax.bar(r1, precision, color='#99ff99', width=bar_width, edgecolor='grey', label='P')
bars2 = ax.bar(r2, recall, color='#FF878B', width=bar_width, edgecolor='grey', label='R')
bars3 = ax.bar(r3, f1_score, color='#3ea8ef', width=bar_width, edgecolor='grey', label='F1')

ax.set_xlabel('Tools',fontsize=16)
ax.set_xticks([r + bar_width for r in range(len(tools))])
ax.set_xticklabels(tools, fontsize=14)
ax.grid(True, linestyle='--')

ax.set_ylabel('Score',fontsize=16)

ax.tick_params(axis='y', labelsize=14)

def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{height:.2f}', ha='center', va='bottom', fontsize=14)

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)

ax.legend(loc='upper right', fontsize=14)
plt.show()