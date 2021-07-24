import pandas as pd

df = pd.read_csv('sunburst_coordinates_2.csv', header=None)
df = df.T

number_of_columns = len(df.columns)
counter = 0
while counter<number_of_columns:
    df[number_of_columns + counter/2]= list(zip(df[counter], df[counter + 1]))
    counter+=2
df = df.iloc[:,number_of_columns:]



print(df)