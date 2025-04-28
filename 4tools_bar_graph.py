import matplotlib.pyplot as plt

tools = ['SQ|CQL|SNK', 'SQ|CQL', 'SQ|SNK', 'CQL|SNK']
precision = [0.22388059701492538, 0.32019704433497537, 0.08333333333333333, 0.23255813953488372]
recall = [0.35545023696682465, 0.3080568720379147, 0.052132701421800945, 0.33175355450236965]
f1_score = [0.27472527472527475, 0.3140096618357488, 0.06413994169096209, 0.2734375]

fig, ax = plt.subplots()

bar_width = 0.25

r1 = range(len(tools))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

bars1 = ax.bar(r1, precision, color='#99ff99', width=bar_width, edgecolor='grey', label='P')
bars2 = ax.bar(r2, recall, color='#FF878B', width=bar_width, edgecolor='grey', label='R')
bars3 = ax.bar(r3, f1_score, color='#3ea8ef', width=bar_width, edgecolor='grey', label='F1')

ax.set_xlabel('Tools', fontweight='bold')
ax.set_xticks([r + bar_width for r in range(len(tools))])
ax.set_xticklabels(tools)
ax.grid(True, linestyle='--')

ax.set_ylabel('Score')

def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{height:.2f}', ha='center', va='bottom', fontsize=10)

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)

ax.legend(loc='lower right')
plt.show()
