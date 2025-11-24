import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#reading csv
df = pd.read_csv('/content/Sleep_health_and_lifestyle_dataset.csv')

#seaborn style
sns.set(style='whitegrid')

###########
#Bar_plots#
###########

#age and sleep duration
plt.figure(figsize=(10,6))
sns.barplot(x='Age',y='Sleep Duration',data = df)
plt.title('comparison of age and sleep duration (bar_plot)')
plt.xlabel('person/s age')
plt.ylabel('sleep time')
plt.show()