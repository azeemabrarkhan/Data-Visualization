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
    3.519668737060042, 1.2008281573498967, 1.2008281573498967, 1.2008281573498967,
    1.2008281573498967, 0, 2.946859903381643, 4.074074074074073, 2.1739130434782608,
    0.4830917874396135, 0.9339774557165861, 1.2008281573498967, 5.371520588911893,
    0, 0, 0, 0, 0, 0.16103059581320447, 0.16103059581320447, 0.4830917874396135,
    0, 0, 0.16103059581320447, 0, 2.7053140096618367, 0, 0, 0.4830917874396135,
    0.4830917874396135, 0, 0, 0, 0, 0.7729468599033814, 0.4830917874396135
]

cwe_codes_snk = [
    "CWE-020", "CWE-022", "CWE-023", "CWE-036", "CWE-073", "CWE-074", "CWE-078",
    "CWE-079", "CWE-088", "CWE-089", "CWE-094", "CWE-099", "CWE-116", "CWE-125",
    "CWE-126", "CWE-200", "CWE-250", "CWE-290", "CWE-312", "CWE-315", "CWE-327",
    "CWE-338", "CWE-352", "CWE-359", "CWE-399", "CWE-400", "CWE-404", "CWE-444",
    "CWE-502", "CWE-601", "CWE-668", "CWE-754", "CWE-770", "CWE-807", "CWE-829",
    "CWE-915", "CWE-918"
]

detection_rates_snk = [
    0, 0.8695652173913042, 0.38647342995169087, 0.38647342995169087, 0.38647342995169087,
    0, 0.24154589371980675, 1.2077294685990336, 0.24154589371980675, 0, 0, 0.38647342995169087,
    1.2077294685990339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

min_length = min(len(detection_rates), len(detection_rates_snk))

detection_rates = detection_rates[:min_length]
detection_rates_snk = detection_rates_snk[:min_length]
cwe_codes = cwe_codes[:min_length]

indices_sorted = np.argsort(detection_rates)

cwe_codes_sorted = [cwe_codes[i] for i in indices_sorted]
detection_rates_sorted_cql = [detection_rates[i] for i in indices_sorted]
detection_rates_sorted_snk = [detection_rates_snk[i] for i in indices_sorted]

plt.figure(figsize=(10, 6))

bar_width = 0.35
index = np.arange(len(cwe_codes_sorted))

plt.bar(index - bar_width/2, detection_rates_sorted_cql, bar_width, color='#3ea8ef', edgecolor='gray', label='CQL')

plt.bar(index + bar_width/2, detection_rates_sorted_snk, bar_width, color='#FF878B', edgecolor='gray', label='SNK')

plt.ylabel('Weighted Detection Percentage', fontsize=14)
plt.xlabel('CWE Identifiers', fontsize=14)

plt.xticks(index, cwe_codes_sorted, rotation=90, fontsize=12)
plt.yticks(fontsize=12)
# plt.grid(True, linestyle='--')

plt.legend( fontsize=12)
plt.tight_layout()

plt.show()