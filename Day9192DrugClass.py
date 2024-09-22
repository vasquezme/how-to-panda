import pandas as pd
import numpy as np

df = pd.read_csv('day9192DrugClass.csv')

df.head()
df.tail()
df.describe()

df.info()
df.dtypes

mean_value = df['Age'].mean()
print("Mean is:", mean_value)

mean_value = df["Na_to_K"].mean()
print("Mean is:", mean_value)

count_sex = df['Sex'].count()
print("Count of everyone is:", count_sex)

count_gender = df.groupby('Sex').size()
print("Count by gender:", count_gender)

count_bp = df.groupby('BP').count()
print('Count by BP :', count_bp)

cholesterol_count = df.groupby('Cholesterol').count()
print('Count by Cholesterol :', cholesterol_count)

drug_count = df.groupby('Drug').count()
print('Count by Drug:', drug_count)
