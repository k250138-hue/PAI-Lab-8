
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data(1).csv")

# a. Filter required scenario
data = df[df['scenario'] == '04_CustAgeDist']

# b. Create histogram with KDE
sns.histplot(
    data=data,
    x='prep_course',
    hue='study_hours',
    bins=5,
    kde=True
)

# c. Customize plot
plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")

# d. Display graph
plt.show()
