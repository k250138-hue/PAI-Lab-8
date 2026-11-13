
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# a. Filter required scenario
data = df[df['scenario'] == '02_MonthlySales']

# b. Group data by company
techstore = data[data['school_type' ] == 'TechStore']
apparelco = data[data['school_type'] == 'ApparelCo']

# c. Plot line chart
plt.plot(techstore['study_hours'], techstore['exam_score'],
         marker='o', label='TechStore')

plt.plot(apparelco['study_hours'], apparelco['exam_score'],
         marker='o', label='ApparelCo')

# d. Customize plot
plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")

# e. Display legend
plt.legend()

# f. Display graph
plt.show()
