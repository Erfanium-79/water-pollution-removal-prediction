import pandas as pd 
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('book1.csv')
df = df.drop(columns=['f1', 'f2', 'f3'])

le = LabelEncoder()
df['Catalyst'] = le.fit_transform(df['Catalyst'])

df.to_csv('dataset.csv', index=False)