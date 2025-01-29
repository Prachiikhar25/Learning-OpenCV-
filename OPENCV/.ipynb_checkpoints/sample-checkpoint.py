import pandas as pd
import numpy as np

# Create a NumPy array of random numbers
data = np.random.randint(10, 100, (5, 3))  # 5 rows, 3 columns

# Create a Pandas DataFrame using the NumPy array
df = pd.DataFrame(data, columns=['Math', 'Science', 'English'])

# Display the DataFrame
print("Original DataFrame:\n", df)

# Add a new column 'Total' which is the sum of all subjects
df['Total'] = df.sum(axis=1)

# Add a new column 'Average' which is the mean of all subjects
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Filter students who scored above 50 in Science
filtered_df = df[df['Science'] > 50]

print("\nDataFrame After Adding Total & Average:\n", df)
print("\nStudents who scored above 50 in Science:\n", filtered_df)
