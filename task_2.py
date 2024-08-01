import pandas as pd

# Load CSV file into DataFrame
df = pd.read_csv('Book1.csv')

# Filter data where age > 30
filtered_df = df[df['age'] > 30]

# Handle missing values by filling them with the mean of the column
df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].mean())

# Calculate summary statistics
summary_stats = df.describe()
mean_age = df['age'].mean()
median_salary = df['salary'].median()
mode_department = df['department'].mode()[0]

# Print results
print("Summary Statistics:\n", summary_stats)
print("Mean Age:", mean_age)
print("Median Salary:", median_salary)
print("Mode Department:", mode_department)
