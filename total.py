import matplotlib.pyplot as plt
import numpy as np

cwe_codes = [
    "CWE-020", "CWE-022", "CWE-023", "CWE-036", "CWE-073", "CWE-074", "CWE-078",
    "CWE-079", "CWE-088", "CWE-089", "CWE-094", "CWE-099", "CWE-116", "CWE-125",
    "CWE-126", "CWE-200", "CWE-250", "CWE-290", "CWE-312", "CWE-315", "CWE-327",
    "CWE-338", "CWE-352", "CWE-359", "CWE-399", "CWE-400", "CWE-404", "CWE-444",
    "CWE-502", "CWE-601", "CWE-668", "CWE-754", "CWE-770", "CWE-807", "CWE-829",
    "CWE-915", "CWE-918"
]

detection_rates = [
    15, 28, 21, 21, 21, 1, 47, 75, 25, 4, 35, 21, 56, 1, 1, 3, 1, 1, 3, 3, 1,
    1, 2, 3, 1, 51, 1, 1, 1, 6, 2, 1, 3, 1, 1, 22, 4
]

indices_sorted = np.argsort(detection_rates)

cwe_codes_sorted = [cwe_codes[i] for i in indices_sorted]
detection_rates_sorted_cql = [detection_rates[i] for i in indices_sorted]

plt.figure(figsize=(10, 6))

bar_width = 0.35
index = np.arange(len(cwe_codes_sorted))

bars = plt.bar(index, detection_rates_sorted_cql, bar_width, color='#3ea8ef', edgecolor='gray', label='CQL')

plt.ylabel('Total number of vulnerabilities per CWE', fontsize=14)
plt.xlabel('CWE Identifiers', fontsize=14)

plt.xticks(index, cwe_codes_sorted, rotation=90, fontsize=12)
plt.yticks(fontsize=12)

for bar, value in zip(bars, detection_rates_sorted_cql):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{value}', 
             ha='center', va='bottom', fontsize=10)

# plt.legend(fontsize=12)
plt.tight_layout()

plt.show()