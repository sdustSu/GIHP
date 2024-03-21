import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

# Read data from CSV file
data = pd.read_csv('PMID30150660_patient_survival_not_benefit.csv')

# Separate the data into two groups
group1 = data[data['GIHP'] == 'N']
group2 = data[data['GIHP'] == 'Y']

# Fit Kaplan-Meier survival curves for each group
kmf = KaplanMeierFitter()

#kmf.fit(group1['SURVIVAL_MONTHS'], event_observed=group1['SURVIVAL_EVENT'], label='Y')
kmf.fit(group1['SURVIVAL_MONTHS'], event_observed=group1['SURVIVAL_EVENT'], label='with mutation')
kmf.plot()

#kmf.fit(group2['SURVIVAL_MONTHS'], event_observed=group2['SURVIVAL_EVENT'], label='N')
kmf.fit(group2['SURVIVAL_MONTHS'], event_observed=group2['SURVIVAL_EVENT'], label='without mutation')
kmf.plot()

# Perform the log-rank test
results = logrank_test(group1['SURVIVAL_MONTHS'], group2['SURVIVAL_MONTHS'], event_observed_A=group1['SURVIVAL_EVENT'], event_observed_B=group2['SURVIVAL_EVENT'])
p_value = results.p_value
print(p_value)
# Add p-value to the plot
plt.text(0.5, 0.8, f'p-value = {p_value:.2e}', transform=plt.gca().transAxes)
plt.xlabel('Time (months)')
plt.ylabel('Survival Probability')
# Save the plot to a PDF file
plt.savefig('PMID30150660_curve_not_benefit.pdf')