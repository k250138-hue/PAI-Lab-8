
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Filter the required scenario
data = df[df['scenario'] == '01_StudyVsScore']

# Create scatter plot
sns.scatterplot(
    data=data,
    x='study_hours',
    y='exam_score',
    hue='prep_course',
    style='prep_course'
)

# Customize plot
plt.title("Study Hours vs. Exam Score by Prep Course Status")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

# Enable gridlines
plt.grid(True)

# Display plot
plt.show()
