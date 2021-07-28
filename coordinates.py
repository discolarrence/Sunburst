import pandas as pd


def filter_coordinates(dataframe, column_contains: str):
    """Selects columns with str in header and returns as ints with no nulls.
    """
    filtered = dataframe.loc[:, dataframe.columns.str.contains(column_contains)]
    nulls_removed = filtered.dropna(axis=0)
    all_ints = nulls_removed.astype(int)
    return all_ints


def make_coordinates_list(dataframe, coordinates_list):
    """Stores merged columns as list. Appends to coordinates_list.
    """
    number_of_columns = len(dataframe.columns)
    counter = 0
    while counter < number_of_columns:
        x_value_index = counter
        y_value_index = counter + 1
        x_y_coordinates = list(zip(dataframe.iloc[:, x_value_index],
                                   dataframe.iloc[:, y_value_index]))
        coordinates_list.append(x_y_coordinates)
        counter += 2


df = pd.read_csv('sunburst_coordinates_2.csv', header=None)
df = df.T
df.columns = df.iloc[0]
df = df.drop(df.index[0])

df_level_one = filter_coordinates(df, '1')
df_level_two = filter_coordinates(df, '2')
df_level_three = filter_coordinates(df, '3')

light_shape_corner_coordinates = []

make_coordinates_list(df_level_one, light_shape_corner_coordinates)
make_coordinates_list(df_level_two, light_shape_corner_coordinates)
make_coordinates_list(df_level_three, light_shape_corner_coordinates)
