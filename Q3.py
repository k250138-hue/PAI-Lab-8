
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# a. Filter required scenario
data = df[df['scenario'] == '03_SalaryDiff']

# b. Set experience level order
order = ['Entry', 'Mid', 'Senior']

# c. Create box plot
sns.boxplot(
    data=data,
    x='prep_course',
    y='exam_score',
    order=order,
    palette='Set2'
)

# d. Customize plot
plt.title("Salary Spread Across Experience Levels")
plt.xlabel("Experience Level")
plt.ylabel("Salary ($)")

# e. Display graph
plt.show()
