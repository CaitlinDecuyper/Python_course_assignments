# homework Session 5 - Caitlin Decuyper

# The homework exercise for this class is to use the data you collected from your experiment and to explore it, possibly clean it,
# and plot the main contrast of interest in a sensible way.
# This applies to both the picture verification task (e.g. matching vs. nonmatching) and the lexical decision task (e.g. word frequency).


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# read example data
data = pd.read_csv('K:\PhD\IMPRScourses\Python\session5\lexical-decision-master\lexdec_results.csv')

# print average RT + sd per word frequency condition
summary = data.groupby(by='frequency').aggregate(
    mean_RT=pd.NamedAgg('reaction_time', np.mean),
    std_RT=pd.NamedAgg('reaction_time', np.std),
)
print(summary)

# remove inaccurate responses
correct_responses = data['accuracy'] == 1
data_correct = data[correct_responses]

# plot RT per word frequency condition
sns.boxplot(x = 'frequency', y = 'reaction_time', data = data_correct)
plt.show()

# plot RT per participant per condition
sns.boxplot(x = 'subject', y = 'reaction_time', hue = 'frequency', data = data_correct)
plt.show()