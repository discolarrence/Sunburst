import csv

with open("sunburst_coordinates_2.csv") as coordinates_file:
    coordinates_rows = csv.reader(coordinates_file)
    coordinates_rows_list = list(coordinates_rows)

#merge rows into lists of x&y coordinates for each shape
#empty master list of all shape coordinates
list_of_coordinates_lists = []
counter = 0
#loop to append eash shape's list of coordinates to the master list
while counter < len(coordinates_rows_list):
    #empty list for coordinates for each shape
    coordinates_set = []
    #loop to append coordinates to a shape's list
    for i in range(0, len(coordinates_rows_list[counter])):
        try:
            x_coordinate = int(coordinates_rows_list[counter][i])
            y_coordinate = int(coordinates_rows_list[counter + 1][i])
            #ignores duplicate coordinate sets for each shape--int() was converting empty strings to the previous cell's value
            coordinates_set.append((x_coordinate, y_coordinate)) if (x_coordinate, y_coordinate) not in coordinates_set else None
        # ignore values that can't be converted to an int
        except ValueError:
            pass     
    list_of_coordinates_lists.append(coordinates_set)
    counter += 2
