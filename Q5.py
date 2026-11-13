
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# a. Filter required scenario
data = df[df['scenario'] == '05_AdVsRevenue']

# b. Create regression plot
sns.regplot(
    data=data,
    x='study_hours',
    y='exam_score',
    color='darkgreen',
    marker='+'
)

# c. Customize plot
plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")

# d. Enable gridlines
plt.grid(True)

# e. Display graph
plt.show()
