import pandas as pd

df = pd.read_csv('sunburst_coordinates_2.csv', header=None)
df = df.T
df.columns = df.iloc[0]
df = df.drop(df.index[0])

df_level_one = df.loc[:, df.columns.str.contains('1')].astype(int)
df_level_two = df.loc[:, df.columns.str.contains('2')].astype(int)
df_level_three = df.loc[:, df.columns.str.contains('3')].dropna(axis=0).astype(int)

coordinates_list = []

def make_coordinates_list(dataframe):
    number_of_columns = len(dataframe.columns)
    counter = 0
    while counter < number_of_columns:
        x_value_index = counter
        y_value_index = counter + 1
        light_shape_coordinates= list(zip(dataframe.iloc[:, x_value_index], dataframe.iloc[:, y_value_index]))
        coordinates_list.append(light_shape_coordinates)
        counter += 2

make_coordinates_list(df_level_one)
make_coordinates_list(df_level_two)
make_coordinates_list(df_level_three)