import matplotlib.pyplot as plt

true_positives = [3, 78, 38]
false_positives = [0, 0, 0]
false_negatives = [194, 119, 159]

labels = ['TP', 'FP', 'FN']
colors = ['#99ff99', '#FF878B', '#3ea8ef']

def generate_labels(sizes):
    return [f'{labels[i]}: {sizes[i]}' if sizes[i] != 0 else '' for i in range(len(sizes))]

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

sonarqube_sizes = [true_positives[0], false_positives[0], false_negatives[0]]
axs[0].pie(sonarqube_sizes, labels=generate_labels(sonarqube_sizes), colors=colors, textprops={'fontsize': 20})
axs[0].set_title('SQ', fontsize=24)

codeql_sizes = [true_positives[1], false_positives[1], false_negatives[1]]
axs[1].pie(codeql_sizes, labels=generate_labels(codeql_sizes), colors=colors, textprops={'fontsize': 20})
axs[1].set_title('CQL', fontsize=24)

snyk_sizes = [true_positives[2], false_positives[2], false_negatives[2]]
axs[2].pie(snyk_sizes, labels=generate_labels(snyk_sizes), colors=colors, textprops={'fontsize': 20})
axs[2].set_title('SNK', fontsize=24)

plt.show()