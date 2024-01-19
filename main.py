import matplotlib.pyplot as plt
import pandas as pd

# Load data from Excel
data = pd.read_excel(r'D:\FILES NI MIGUEL\pythonProject\restaurant_data.xlsx')

# Select rows 700 to 720
selected_data = data.iloc[1:50]

# Plot using Matplotlib
plt.bar(selected_data['district_name'], selected_data.index)
plt.ylabel('Row Index')
plt.xlabel("District Name")
plt.title('Bar Graph using Matplotlib for Rows 1-49')

plt.xticks(rotation=40, ha='right', fontsize=6)

plt.show()
