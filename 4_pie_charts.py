import matplotlib.pyplot as plt

true_positives = [95, 80, 39, 94]
false_positives = [0, 0, 0, 0]
false_negatives = [102, 117, 158, 103]

labels = ['TP', 'FP', 'FN']
colors = ['#99ff99', '#FF878B', '#3ea8ef']

def generate_labels(sizes):
    return [f'{labels[i]}: {sizes[i]}' if sizes[i] != 0 else '' for i in range(len(sizes))]

fig, axs = plt.subplots(1, 4, figsize=(20, 5))

sonarqubeAndCodeQLAndSnyk_sizes = [true_positives[0], false_positives[0], false_negatives[0]]
axs[0].pie(sonarqubeAndCodeQLAndSnyk_sizes, labels=generate_labels(sonarqubeAndCodeQLAndSnyk_sizes), colors=colors, textprops={'fontsize': 20})
axs[0].set_title('SQ|CQL|SNK', fontsize=24)


sonarqubeAndCodeQL_sizes = [true_positives[1], false_positives[1], false_negatives[1]]
axs[1].pie(sonarqubeAndCodeQL_sizes, labels=generate_labels(sonarqubeAndCodeQL_sizes), colors=colors, textprops={'fontsize': 20})
axs[1].set_title('SQ|CQL', fontsize=24)


sonarqubeAndSnyk_sizes = [true_positives[2], false_positives[2], false_negatives[2]]
axs[2].pie(sonarqubeAndSnyk_sizes, labels=generate_labels(sonarqubeAndSnyk_sizes), colors=colors, textprops={'fontsize': 20})
axs[2].set_title('SQ|SNK', fontsize=24)


codeQlAndSnyk_sizes = [true_positives[3], false_positives[3], false_negatives[3]]
axs[3].pie(codeQlAndSnyk_sizes, labels=generate_labels(codeQlAndSnyk_sizes), colors=colors, textprops={'fontsize': 20})
axs[3].set_title('CQL|SNK', fontsize=24)

plt.show()